"""Support for Névnap sensors."""
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
from homeassistant.helpers.entity import EntityCategory
from . import DOMAIN

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(hours=1)
API_URL = "https://api.omw.hu/nevnap.php"

SENSOR_TYPES: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        key="nevnap_elso",
        name="Névnap elsődleges",
        icon="mdi:party-popper",
    ),
    SensorEntityDescription(
        key="nevnap_masodik",
        name="Névnap másodlagos",
        icon="mdi:party-popper",
    ),
    SensorEntityDescription(
        key="egyeb_nevnapok",
        name="Egyéb Névnapok",
        icon="mdi:party-popper",
    ),
)

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Névnap sensor."""
    async_add_entities([
        NevnapSensor(hass, config_entry, "Névnap elsődleges", "nevnap_ma", 0),
        NevnapSensor(hass, config_entry, "Névnap másodlagos", "nevnap_ma", 1),
        NevnapSensor(hass, config_entry, "Egyéb Névnapok", "egyeb_ma", None)
    ], True)

class NevnapSensor(SensorEntity):
    """Implementation of a Névnap sensor."""

    _attr_has_entity_name = True
    _attr_icon = "mdi:party-popper"
    _attr_entity_category = None  # Ez biztosítja, hogy szolgáltatásként jelenjen meg

    def __init__(
        self,
        hass: HomeAssistant,
        config_entry: ConfigEntry,
        name: str,
        data_key: str,
        name_index: int | None
    ) -> None:
        """Initialize the sensor."""
        self.hass = hass
        self._config_entry = config_entry
        self._name = name
        self._data_key = data_key
        self._name_index = name_index
        self._state: StateType = None
        self._available = True
        self._attr_extra_state_attributes = {}
        
        # Egyedi azonosító beállítása
        base_id = "nevnap"
        if name_index is not None:
            self._attr_unique_id = f"{base_id}_{name.lower().replace(' ', '_')}"
        else:
            self._attr_unique_id = f"{base_id}_egyeb"

        # Szolgáltatás név beállítása
        self._attr_entity_registry_enabled_default = True
        self._attr_entity_registry_visible_default = True
        self._attr_name = f"Magyar névnap {name}"

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
                            
                            if self._name_index is not None:
                                names = [name.strip() for name in value.split(",")]
                                
                                if self._name_index < len(names):
                                    self._state = names[self._name_index]
                                else:
                                    self._state = "nincs" if self._name_index == 1 else names[0]
                            else:
                                self._state = value
                            
                            self._available = True
                        else:
                            _LOGGER.error("Failed to get data from API: %s", response.status)
                            self._available = False
        except Exception as error:
            _LOGGER.error("Error updating Névnap sensor: %s", error)
            self._available = False