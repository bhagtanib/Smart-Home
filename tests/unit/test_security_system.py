import unittest
from devices.security_system import SecuritySystem

class TestSecuritySystem(unittest.TestCase):
    def setUp(self):
        self.security_system = SecuritySystem(device_id=1, name="Test Security System")

    def test_initial_state(self):
        self.assertEqual(self.security_system.get_status(), "off, Armed: False, Sensors: []")

    def test_arm(self):
        self.security_system.arm()
        self.assertEqual(self.security_system.get_status(), "off, Armed: True, Sensors: []")

    def test_disarm(self):
        self.security_system.arm()
        self.security_system.disarm()
        self.assertEqual(self.security_system.get_status(), "off, Armed: False, Sensors: []")

    def test_add_sensor(self):
        self.security_system.add_sensor("Door Sensor")
        self.assertEqual(self.security_system.get_status(), "off, Armed: False, Sensors: ['Door Sensor']")

if __name__ == '__main__':
    unittest.main()
