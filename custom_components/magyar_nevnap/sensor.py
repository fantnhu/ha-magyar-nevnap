from homeassistant.components.sensor import SensorDeviceClass, SensorEntity
from homeassistant.const import EntityCategory

from .const import DOMAIN
from .coordinator import split_names
from .entity import NevnapEntity


async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([
        NevnapSensor(entry.runtime_data, "nevnap_ma", "kiemelt_nevnap", "kiemelt_névnap"),
        NevnapSensor(entry.runtime_data, "egyeb_ma", "masodlagos_nevnap", "másodlagos_névnap"),
        LastUpdateSensor(entry.runtime_data),
    ])


class NevnapSensor(NevnapEntity, SensorEntity):
    _attr_icon = "mdi:party-popper"

    def __init__(self, coordinator, data_key, translation_key, legacy_id):
        super().__init__(coordinator)
        self.data_key = data_key
        self._attr_translation_key = translation_key

        self._attr_unique_id = f"{DOMAIN}_{legacy_id}"

    @property
    def native_value(self):
        value = self.coordinator.data[self.data_key]
        return value if len(value) <= 255 else value[:254] + "…"

    @property
    def extra_state_attributes(self):
        value = self.coordinator.data[self.data_key]
        return {"names": split_names(value), "full_text": value}


class LastUpdateSensor(NevnapEntity, SensorEntity):
    _attr_translation_key = "last_successful_update"
    _attr_device_class = SensorDeviceClass.TIMESTAMP
    _attr_entity_category = EntityCategory.DIAGNOSTIC
    _attr_entity_registry_enabled_default = False

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = f"{DOMAIN}_last_successful_update"

    @property
    def available(self):
        return self.coordinator.last_successful_update is not None

    @property
    def native_value(self):
        return self.coordinator.last_successful_update
