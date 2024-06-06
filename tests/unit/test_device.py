import unittest
from devices.device import Device

class TestDevice(unittest.TestCase):
    def setUp(self):
        self.device = Device(device_id=1, name="Generic Device")

    def test_initial_state(self):
        self.assertEqual(self.device.get_status(), "off")

    def test_turn_on(self):
        self.device.turn_on()
        self.assertEqual(self.device.get_status(), "on")

    def test_turn_off(self):
        self.device.turn_on()
        self.device.turn_off()
        self.assertEqual(self.device.get_status(), "off")

if __name__ == '__main__':
    unittest.main()
