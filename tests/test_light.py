import unittest
from devices.light import Light

class TestLight(unittest.TestCase):
    def setUp(self):
        self.light = Light(device_id=1, name="Test Light")

    def test_initial_state(self):
        self.assertEqual(self.light.get_status(), "off, Brightness: 100, Color: white")

    def test_turn_on(self):
        # Test turning on the light
        self.light.turn_on()
        self.assertEqual(self.light.get_status(), "on, Brightness: 100, Color: white")

    def test_turn_off(self):
        # Test turning off the light
        self.light.turn_on()  # Turn on the light first
        self.light.turn_off()
        self.assertEqual(self.light.get_status(), "off, Brightness: 100, Color: white")

    def test_set_brightness_when_off(self):
        # Test setting brightness of the light
        self.light.turn_off()
        self.light.set_brightness(50)
        self.assertEqual(self.light.get_status(), "off, Brightness: 50, Color: white")
    def test_set_brightness_when_on(self):
        # Test setting brightness of the light
        self.light.turn_on()
        self.light.set_brightness(50)
        self.assertEqual(self.light.get_status(), "on, Brightness: 50, Color: white")

if __name__ == '__main__':
    unittest.main()
