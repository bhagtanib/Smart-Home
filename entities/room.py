class Room:
    def __init__(self, room_id, name, logger=None):
        self.room_id = room_id
        self.name = name
        self.devices = []
        self.logger = logger

    def add_device(self, device):
        if device not in self.devices:
            self.devices.append(device)
            print(f"Device '{device.name}' added to room {self.name}.")
            if self.logger:  # Check if logger exists before logging
                self.logger.log_event(f"Device '{device.name}' added to room {self.name}.")

    def remove_device(self, device):
        if device in self.devices:
            self.devices.remove(device)
            print(f"Device '{device.name}' removed from room {self.name}.")
            if self.logger:  # Check if logger exists before logging
                self.logger.log_event(f"Device '{device.name}' removed from room {self.name}.")
