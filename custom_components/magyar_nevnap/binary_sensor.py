from homeassistant.components.binary_sensor import BinarySensorEntity

from .const import CONF_INCLUDE_SECONDARY, CONF_WATCHED_NAMES, DOMAIN
from .coordinator import split_names
from .entity import NevnapEntity


async def async_setup_entry(hass, entry, async_add_entities):
    if split_names(entry.options.get(CONF_WATCHED_NAMES, "")):
        async_add_entities([WatchedNamedaySensor(entry.runtime_data)])


class WatchedNamedaySensor(NevnapEntity, BinarySensorEntity):
    _attr_translation_key = "watched_nameday"
    _attr_icon = "mdi:account-heart"

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = f"{DOMAIN}_watched_nameday"

    @property
    def matched_names(self):
        options = self.coordinator.config_entry.options
        watched = {name.casefold() for name in split_names(options.get(CONF_WATCHED_NAMES, ""))}
        text = self.coordinator.data["nevnap_ma"]
        if options.get(CONF_INCLUDE_SECONDARY, True):
            text += "," + self.coordinator.data["egyeb_ma"]
        return [name for name in split_names(text) if name.casefold() in watched]

    @property
    def is_on(self):
        return bool(self.matched_names)

    @property
    def extra_state_attributes(self):
        return {"matched_names": self.matched_names}
