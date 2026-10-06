from __future__ import annotations

import asyncio
from datetime import datetime, timedelta
import logging
import re
import unicodedata
from typing import Any

import aiohttp
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.util import dt as dt_util

from .const import API_URL, CONF_UPDATE_INTERVAL, DEFAULT_UPDATE_INTERVAL, DOMAIN

_LOGGER = logging.getLogger(__name__)


def split_names(value: str) -> list[str]:

    result = []
    seen = set()
    for part in re.split(r"[,;\n]+", unicodedata.normalize("NFC", value)):
        name = part.strip()
        if name and name.casefold() not in seen:
            seen.add(name.casefold())
            result.append(name)
    return result


def parse_payload(payload: Any) -> dict[str, str]:

    if not isinstance(payload, dict):
        raise ValueError("Expected a nameday object")
    result = {}
    for key in ("nevnap_ma", "egyeb_ma"):
        value = payload.get(key)
        if not isinstance(value, str):
            raise ValueError(f"Missing or invalid {key}")
        result[key] = value.strip()
    if not result["nevnap_ma"]:
        raise ValueError("Empty primary nameday")
    return result


class NevnapCoordinator(DataUpdateCoordinator[dict[str, str]]):
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        super().__init__(
            hass, _LOGGER, name=DOMAIN, config_entry=entry,
            update_interval=timedelta(minutes=entry.options.get(
                CONF_UPDATE_INTERVAL, DEFAULT_UPDATE_INTERVAL)),
        )
        self.session = async_get_clientsession(hass)
        self.last_successful_update: datetime | None = None

    @property
    def is_current_day(self) -> bool:


        return self.last_successful_update is not None and (
            dt_util.as_local(self.last_successful_update).date() == dt_util.now().date()
        )

    async def _async_update_data(self) -> dict[str, str]:
        try:
            async with asyncio.timeout(10):
                async with self.session.get(API_URL) as response:
                    response.raise_for_status()
                    data = parse_payload(await response.json())
        except TimeoutError as err:
            raise UpdateFailed("Nameday request timed out") from err
        except aiohttp.ClientError as err:
            raise UpdateFailed("Unable to fetch namedays") from err
        except (ValueError, TypeError) as err:
            raise UpdateFailed("Invalid nameday response") from err
        self.last_successful_update = dt_util.utcnow()
        return data
