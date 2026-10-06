from datetime import timedelta

from homeassistant.components.calendar import CalendarEntity, CalendarEvent
from homeassistant.util import dt as dt_util

from .const import DOMAIN
from .entity import NevnapEntity


async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([MagyarNevnapCalendar(entry.runtime_data)])


class MagyarNevnapCalendar(NevnapEntity, CalendarEntity):
    _attr_translation_key = "magyar_nevnapok"
    _attr_icon = "mdi:calendar-heart"

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = f"{DOMAIN}_calendar"

    @property
    def event(self):
        if not self.available:
            return None
        today = dt_util.now().date()
        primary = self.coordinator.data["nevnap_ma"]
        secondary = self.coordinator.data["egyeb_ma"]
        description = f"Kiemelt névnap: {primary}"
        if secondary:
            description += f"\nTovábbi névnapok: {secondary}"
        return CalendarEvent(
            summary=primary, start=today, end=today + timedelta(days=1),
            description=description,
        )

    async def async_get_events(self, hass, start_date, end_date):
        event = self.event
        if event is None or end_date <= start_date:
            return []
        start = dt_util.start_of_local_day(event.start)
        end = dt_util.start_of_local_day(event.end)
        return [event] if start < end_date and end > start_date else []
