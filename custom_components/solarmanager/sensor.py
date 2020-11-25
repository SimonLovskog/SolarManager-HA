"""Platform for sensor integration."""
from homeassistant.const import PERCENTAGE, POWER_WATT
from homeassistant.helpers.entity import Entity

from datetime import timedelta

from .base import getData

SCAN_INTERVAL = timedelta(seconds=2)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the uptime sensor platform."""

    host = config_entry.data['host']

    async_add_entities([
        BatteryPercentSensor(host),
        BatteryPowerSensor(host),
        LoadPowerSensor(host),
        PVPowerSensor(host)
    ], True)

class BatteryPercentSensor(Entity):
    """Representation of an uptime sensor."""

    @property
    def unique_id(self):
        """Return unique ID for device."""
        return self._unique_id

    def __init__(self, host):
        """Initialize the uptime sensor."""
        self._name = "BatteryPercent"
        self._unique_id = "solarmanager-batterypercent"
        self._state = None
        self.host = host

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def icon(self):
        """Icon to display in the front end."""
        return "mdi:battery"

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement the value is expressed in."""
        return PERCENTAGE

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Update the state of the sensor."""
        response = await getData(self.host)

        self._state = response['battery']['percent']

class BatteryPowerSensor(Entity):
    """Representation of an uptime sensor."""

    def __init__(self, host):
        """Initialize the uptime sensor."""
        self._name = "BatteryPower"
        self._unique_id = "solarmanager-batterypower"
        self._state = None
        self.host = host

    @property
    def unique_id(self):
        """Return unique ID for device."""
        return self._unique_id

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def icon(self):
        """Icon to display in the front end."""
        return "mdi:battery"

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement the value is expressed in."""
        return POWER_WATT

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Update the state of the sensor."""
        response = await getData(self.host)

        self._state = response['battery']['power']

class LoadPowerSensor(Entity):
    """Representation of an uptime sensor."""

    def __init__(self, host):
        """Initialize the uptime sensor."""
        self._name = "LoadPower"
        self._state = None
        self.host = host
        self._unique_id = "solarmanager-loadpower"

    @property
    def unique_id(self):
        """Return unique ID for device."""
        return self._unique_id

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def icon(self):
        """Icon to display in the front end."""
        return "mdi:highlight"

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement the value is expressed in."""
        return POWER_WATT

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Update the state of the sensor."""
        response = await getData(self.host)

        self._state = response['load']['power']
    
class PVPowerSensor(Entity):
    """Representation of an uptime sensor."""

    def __init__(self, host):
        """Initialize the uptime sensor."""
        self._name = "PVPower"
        self._state = None
        self.host = host
        self._unique_id = "solarmanager-pvpower"

    @property
    def unique_id(self):
        """Return unique ID for device."""
        return self._unique_id

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def icon(self):
        """Icon to display in the front end."""
        return "mdi:wb_sunny"

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement the value is expressed in."""
        return POWER_WATT

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Update the state of the sensor."""
        response = await getData(self.host)

        self._state = response['photovoltic']['power']