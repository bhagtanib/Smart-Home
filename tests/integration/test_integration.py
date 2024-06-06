import unittest
from controllers.smart_home_controller import SmartHomeController
from controllers.scheduler import Scheduler
from entities.user import User
from entities.room import Room
from devices.light import Light
from devices.thermostat import Thermostat
from devices.security_system import SecuritySystem
from devices.camera import Camera
from utils.logger import Logger

class TestSmartHomeIntegration(unittest.TestCase):
    def setUp(self):
        self.logger = Logger('smart_home_test.log')

        # Create users
        self.user1 = User(user_id=1, name="John", logger=self.logger)
        self.user2 = User(user_id=2, name="Alice", logger=self.logger)

        # Create rooms
        self.living_room = Room(room_id=1, name="Living Room", logger=self.logger)
        self.bedroom = Room(room_id=2, name="Bedroom", logger=self.logger)

        # Create devices
        self.living_room_light = Light(device_id=1, name="Living Room Light", logger=self.logger)
        self.bedroom_light = Light(device_id=2, name="Bedroom Light", logger=self.logger)
        self.bedroom_thermostat = Thermostat(device_id=3, name="Bedroom Thermostat", logger=self.logger)
        self.home_security = SecuritySystem(device_id=4, name="Home Security System", logger=self.logger)
        self.living_room_security = SecuritySystem(device_id=5, name="Living Room Security System", logger=self.logger)
        self.smart_camera = Camera(device_id=6, name="Smart Camera", location="Front Door", logger=self.logger)

        # Add devices to rooms
        self.living_room.add_device(self.living_room_light)
        self.bedroom.add_device(self.bedroom_light)
        self.bedroom.add_device(self.bedroom_thermostat)

        # Create a smart home controller
        self.smart_home_controller = SmartHomeController(
            devices=[self.living_room_light, self.bedroom_light, self.bedroom_thermostat, self.home_security, self.living_room_security, self.smart_camera],
            users=[self.user1, self.user2],
            rooms=[self.living_room, self.bedroom],
            logger=self.logger
        )

        # Create a scheduler
        self.scheduler = Scheduler(logger=self.logger)

    def test_user_permissions(self):
        self.user1.grant_permission("control_light")
        self.user2.grant_permission("control_thermostat")

        self.assertIn("control_light", self.user1.permissions)
        self.assertIn("control_thermostat", self.user2.permissions)

    def test_device_control(self):
        self.smart_home_controller.control_device(device_id=1, action="turn_on")
        self.assertEqual(self.living_room_light.get_status(), "on, Brightness: 100, Color: white")

        self.smart_home_controller.control_device(device_id=3, action="set_temperature", temp=22)
        self.assertEqual(self.bedroom_thermostat.get_status(), "off, Current Temperature: 20, Target Temperature: 22")

    def test_scheduler_tasks(self):
        self.scheduler.schedule_task("Turn off living room light at 10:00 PM")
        self.scheduler.schedule_task("Arm security system at 11:00 PM")
        self.scheduler.run_tasks()

        self.assertEqual(self.scheduler.tasks, [])

if __name__ == '__main__':
    unittest.main()
