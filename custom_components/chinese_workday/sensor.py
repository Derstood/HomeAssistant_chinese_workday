from workalendar.asia import China
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.event import async_track_time_interval
from datetime import date, timedelta
import logging
_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    async_add_entities([ChinaWorkdaySensor()])

class ChinaWorkdaySensor(Entity):
    def __init__(self):
        self._state = None

    @property
    def name(self):
        return "chinese_workday_sensor"

    @property
    def state(self):
        return self._state

    def update(self):
        cal = China()
        today = date.today()
        self._state = cal.is_working_day(today)
        _LOGGER.warning("ChinaWorkdaySensor just updated")
    @property
    def unique_id(self):
        return "chinese_workday"
        
  
    async def async_added_to_hass(self):
        _LOGGER.warning("ChinaWorkdaySensor async updated start")
        async_track_time_interval(self.hass, self.update, timedelta(hours=1))
        _LOGGER.warning("ChinaWorkdaySensor async updated finish")
