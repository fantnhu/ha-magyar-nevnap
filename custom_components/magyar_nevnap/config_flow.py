import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback

from .const import (
    CONF_INCLUDE_SECONDARY, CONF_UPDATE_INTERVAL, CONF_WATCHED_NAMES,
    DEFAULT_UPDATE_INTERVAL, DOMAIN, NAME,
)


class MagyarNevnapConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()
        if user_input is not None:
            return self.async_create_entry(title=NAME, data={})
        return self.async_show_form(step_id="user", data_schema=vol.Schema({}))

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return NevnapOptionsFlow()


class NevnapOptionsFlow(config_entries.OptionsFlowWithReload):
    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)
        options = self.config_entry.options
        return self.async_show_form(step_id="init", data_schema=vol.Schema({
            vol.Required(CONF_UPDATE_INTERVAL, default=options.get(
                CONF_UPDATE_INTERVAL, DEFAULT_UPDATE_INTERVAL)):
                vol.All(vol.Coerce(int), vol.Range(min=5, max=1440)),
            vol.Optional(CONF_WATCHED_NAMES, default=options.get(CONF_WATCHED_NAMES, "")): str,
            vol.Required(CONF_INCLUDE_SECONDARY, default=options.get(CONF_INCLUDE_SECONDARY, True)): bool,
        }))
