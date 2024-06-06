import unittest
from devices.thermostat import Thermostat

class TestThermostat(unittest.TestCase):
    def setUp(self):
        self.thermostat = Thermostat(device_id=1, name="Test Thermostat")

    def test_initial_state(self):
        self.assertEqual(self.thermostat.get_status(), "off, Current Temperature: 20, Target Temperature: 22")

    def test_set_temperature(self):
        self.thermostat.set_temperature(25)
        self.assertEqual(self.thermostat.get_status(), "off, Current Temperature: 20, Target Temperature: 25")

if __name__ == '__main__':
    unittest.main()
