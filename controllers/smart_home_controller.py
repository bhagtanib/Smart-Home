class SmartHomeController:
    def __init__(self, devices, users, rooms, logger=None):
        self.devices = devices
        self.users = users
        self.rooms = rooms
        self.logger = logger

    def add_device(self, device):
        self.devices.append(device)
        print(f"Device '{device.name}' added to the smart home system.")

    def add_room(self, room):
        self.rooms.append(room)
        print(f"room '{room.name}' added to the smart home system.")

    def remove_device(self, device_id):
        for device in self.devices:
            if device.device_id == device_id:
                self.devices.remove(device)
                print(
                    f"Device '{device.name}' removed from the smart home system.")
                return
        print(f"No device found with ID '{device_id}'.")

    def add_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' added to the smart home system.")

    def remove_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                print(f"User '{user.name}' removed from the smart home system.")
                return
        print(f"No user found with ID '{user_id}'.")

    def control_device(self, device_id, action, **kwargs):
        for device in self.devices:
            if device.device_id == device_id:
                if hasattr(device, action):
                    method = getattr(device, action)
                    if (kwargs):
                        method(kwargs)
                    else:
                        method()
                else:
                    print(
                        f"Action '{action}' not supported for device '{device.name}'.")
                return
        print(f"No device found with ID '{device_id}'.")
