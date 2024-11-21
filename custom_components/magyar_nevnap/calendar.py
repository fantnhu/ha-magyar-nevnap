"""Calendar platform for Magyar Névnap integration."""
from __future__ import annotations

from datetime import datetime, date, timedelta
import logging
from typing import Any

from homeassistant.components.calendar import CalendarEntity, CalendarEvent
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.device_registry import DeviceEntryType
from homeassistant.util import dt as dt_util

from . import DOMAIN
from .sensor import DEVICE_NAME

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Magyar Névnap Calendar."""
    async_add_entities([MagyarNevnapCalendar(hass, config_entry)], True)

class MagyarNevnapCalendar(CalendarEntity):
    """Magyar Névnap Calendar class."""

    _attr_has_entity_name = True

    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None:
        """Initialize the Magyar Névnap Calendar."""
        self.hass = hass
        self._config_entry = config_entry
        self._attr_unique_id = f"{DOMAIN}_calendar"
        self._attr_name = "Magyar névnapok"
        self._event = None
        
        # Device info beállítása
        self._attr_device_info = DeviceInfo(
            entry_type=DeviceEntryType.SERVICE,
            identifiers={(DOMAIN, config_entry.entry_id)},
            name=DEVICE_NAME,
            manufacturer="Magyar névnap szolgáltatás",
            model="Névnap API",
        )

    @property
    def event(self) -> CalendarEvent | None:
        """Return the current event."""
        now = dt_util.now()
        return self._create_event(now.date())

    async def async_get_events(
        self, hass: HomeAssistant, start_date: datetime, end_date: datetime
    ) -> list[CalendarEvent]:
        """Get all events in a specific time frame."""
        events = []
        current_date = start_date.date()
        
        while current_date <= end_date.date():
            if current_date == dt_util.now().date():
                if event := self._create_event(current_date):
                    events.append(event)
            current_date += timedelta(days=1)
            
        return events

    def _create_event(self, event_date: date) -> CalendarEvent | None:
        """Create an event for the given date if it matches today."""
        try:
            # Csak akkor hozzunk létre eseményt, ha a dátum a mai nap
            if event_date == dt_util.now().date():
                # Get state from the kiemelt névnap sensor
                primary_state = self.hass.states.get("sensor.magyar_nevnap_kiemelt_nevnap")
                
                if not primary_state or primary_state.state == "unavailable":
                    return None

                # Create event summary
                summary = f" {primary_state.state}"

                # Create start and end time for the event
                start = datetime.combine(event_date, datetime.min.time())
                start = dt_util.as_local(start)
                end = datetime.combine(event_date, datetime.max.time())
                end = dt_util.as_local(end)

                return CalendarEvent(
                    summary=summary,
                    start=start,
                    end=end,
                    description=f"Mai névnap: {primary_state.state}"
                )
            return None
        except Exception as error:
            _LOGGER.error("Error creating calendar event: %s", error)
            return None