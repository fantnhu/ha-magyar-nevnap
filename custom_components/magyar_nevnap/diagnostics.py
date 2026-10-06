from .const import CONF_INCLUDE_SECONDARY, CONF_UPDATE_INTERVAL, DEFAULT_UPDATE_INTERVAL, VERSION


async def async_get_config_entry_diagnostics(hass, entry):
    coordinator = entry.runtime_data
    return {
        "version": VERSION,
        "update_interval_minutes": entry.options.get(CONF_UPDATE_INTERVAL, DEFAULT_UPDATE_INTERVAL),
        "include_secondary": entry.options.get(CONF_INCLUDE_SECONDARY, True),
        "last_update_success": coordinator.last_update_success,
        "last_successful_update": coordinator.last_successful_update.isoformat()
        if coordinator.last_successful_update else None,
        "current_local_retrieval_day": coordinator.is_current_day,
        "data": coordinator.data,
    }
