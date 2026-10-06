from homeassistant.helpers.device_registry import DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, NAME, VERSION
from .coordinator import NevnapCoordinator


class NevnapEntity(CoordinatorEntity[NevnapCoordinator]):
    _attr_has_entity_name = True

    def __init__(self, coordinator: NevnapCoordinator) -> None:
        super().__init__(coordinator)
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.config_entry.entry_id)},
            name=NAME, manufacturer="fantnhu", model=NAME,
            sw_version=VERSION, entry_type=DeviceEntryType.SERVICE,
        )

    @property
    def available(self) -> bool:
        return super().available and self.coordinator.is_current_day
