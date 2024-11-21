"""Support for Magyar Névnap sensors."""
from __future__ import annotations

from datetime import timedelta
import aiohttp
import async_timeout
import logging

from homeassistant.components.sensor import (
    SensorEntity,
    SensorEntityDescription,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import StateType
from homeassistant.helpers.device_registry import DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo
from . import DOMAIN

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(hours=1)
API_URL = "https://api.omw.hu/nevnap.php"

DEVICE_NAME = "Magyar névnap"

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Magyar Névnap sensor."""
    async_add_entities([
        NevnapSensor(hass, config_entry, "Kiemelt névnap", "nevnap_ma"),
        NevnapSensor(hass, config_entry, "Másodlagos névnap", "egyeb_ma")
    ], True)

class NevnapSensor(SensorEntity):
    """Implementation of a Magyar Névnap sensor."""

    _attr_has_entity_name = True
    _attr_icon = "mdi:party-popper"

    def __init__(
        self,
        hass: HomeAssistant,
        config_entry: ConfigEntry,
        name: str,
        data_key: str,
    ) -> None:
        """Initialize the sensor."""
        self.hass = hass
        self._config_entry = config_entry
        self._name = name
        self._data_key = data_key
        self._state: StateType = None
        self._available = True
        self._attr_extra_state_attributes = {}
        
        # Egyedi azonosító beállítása
        base_id = "magyar_nevnap"
        self._attr_unique_id = f"{base_id}_{name.lower().replace(' ', '_')}"

        # Device info beállítása a szolgáltatásként való megjelenítéshez
        self._attr_device_info = DeviceInfo(
            entry_type=DeviceEntryType.SERVICE,
            identifiers={(DOMAIN, config_entry.entry_id)},
            name=DEVICE_NAME,
            manufacturer="Magyar névnap szolgáltatás",
            model="Névnap API",
        )

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return self._name

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self._available

    @property
    def native_value(self) -> StateType:
        """Return the state of the sensor."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return self._attr_extra_state_attributes

    async def async_update(self) -> None:
        """Get the latest data from the API."""
        try:
            async with async_timeout.timeout(10):
                async with aiohttp.ClientSession() as session:
                    async with session.get(API_URL) as response:
                        if response.status == 200:
                            data = await response.json()
                            value = data.get(self._data_key, "")
                            self._state = value
                            self._available = True
                        else:
                            _LOGGER.error("Failed to get data from API: %s", response.status)
                            self._available = False
        except Exception as error:
            _LOGGER.error("Error updating Magyar Névnap sensor: %s", error)
            self._available = False