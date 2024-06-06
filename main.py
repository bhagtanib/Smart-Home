from entities.user import User
from entities.room import Room
from controllers.smart_home_controller import SmartHomeController
from controllers.scheduler import Scheduler
from devices.light import Light
from devices.thermostat import Thermostat
from devices.security_system import SecuritySystem
from devices.camera import Camera
from utils.logger import Logger  # Import the Logger class
import sys

def main():
    # Create a logger instance
    logger = Logger('smart_home.log')


    # Create users
    user1 = User(user_id=1, name="John", logger=logger)
    user2 = User(user_id=2, name="Alice", logger=logger)

    # Create rooms
    living_room = Room(room_id=1, name="Living Room", logger=logger)
    bedroom = Room(room_id=2, name="Bedroom", logger=logger)

    # Create devices with logger passed down
    living_room_light = Light(device_id=1, name="Living Room Light", logger=logger)
    living_room.add_device(living_room_light)

    bedroom_light = Light(device_id=2, name="Bedroom Light", logger=logger)
    bedroom.add_device(bedroom_light)

    bedroom_thermostat = Thermostat(device_id=3, name="Bedroom Thermostat", logger=logger)
    bedroom.add_device(bedroom_thermostat)

    home_security = SecuritySystem(device_id=4, name="Home Security System", logger=logger)
    living_room_security = SecuritySystem(device_id=5, name="Living Room Security System", logger=logger)
    smart_camera = Camera(device_id=6, name="Smart Camera", location="Front Door", logger=logger)

    # Create a smart home controller
    smart_home_controller = SmartHomeController(devices=[], users=[user1, user2], rooms=[living_room, bedroom], logger=logger)

    # Add devices to the controller
    smart_home_controller.add_device(living_room_light)
    smart_home_controller.add_device(bedroom_light)
    smart_home_controller.add_device(bedroom_thermostat)
    smart_home_controller.add_device(home_security)
    smart_home_controller.add_device(living_room_security)
    smart_home_controller.add_device(smart_camera)

    # Simulate user interactions
    # logger.log_event('Simulation started.')
    user1.grant_permission("control_light")
    user2.grant_permission("control_thermostat")

    smart_home_controller.control_device(device_id=1, action="turn_on")
    smart_home_controller.control_device(device_id=3, action="set_temperature", temp=22)
    smart_home_controller.control_device(device_id=5, action="arm")
    smart_home_controller.control_device(device_id=6, action="start_recording")
    # logger.log_event('User interactions simulated.')

    # Create a scheduler and schedule tasks
    scheduler = Scheduler(logger=logger)
    scheduler.schedule_task("Turn off living room light at 10:00 PM")
    scheduler.schedule_task("Arm security system in the bedroom at 11:00 PM")

    # Run scheduled tasks
    # logger.log_event('Scheduled tasks started.')
    scheduler.run_tasks()
    # logger.log_event('Simulation completed.')



if __name__ == "__main__":
    main()
