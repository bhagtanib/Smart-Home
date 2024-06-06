import unittest
from controllers.smart_home_controller import SmartHomeController
from devices.light import Light
from devices.thermostat import Thermostat
from devices.security_system import SecuritySystem
from devices.camera import Camera
from entities.user import User
from entities.room import Room
from utils.logger import Logger

class TestSmartHomeController(unittest.TestCase):
    def setUp(self):
        self.logger = Logger('smart_home.log')
        self.controller = SmartHomeController(devices=[], users=[], rooms=[], logger=self.logger)
        self.user = User(user_id=1, name="Test User", logger=self.logger)
        self.room = Room(room_id=1, name="Test Room", logger=self.logger)
        self.light = Light(device_id=1, name="Test Light", logger=self.logger)
        self.controller.add_user(self.user)
        self.controller.add_room(self.room)
        self.controller.add_device(self.light)
        self.room.add_device(self.light)

    def test_add_user(self):
        user = User(user_id=2, name="New User", logger=self.logger)
        self.controller.add_user(user)
        self.assertIn(user, self.controller.users)

    def test_control_device(self):
        self.user.grant_permission("control_light")
        self.controller.control_device(device_id=1, action="turn_on")
        self.assertEqual(self.light.get_status(), "on, Brightness: 100, Color: white")

if __name__ == '__main__':
    unittest.main()
