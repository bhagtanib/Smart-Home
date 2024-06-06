from devices.device import Device

class Light(Device):
    def __init__(self, device_id, name, brightness=100, color='white', logger=None):
        super().__init__(device_id, name, logger=logger)  # Pass logger argument to superclass constructor
        self.brightness = brightness
        self.color = color
    
    def set_brightness(self, level):
        self.brightness = level
        print(f"{self.name} brightness set to {self.brightness}.")
        if self.logger:  # Check if logger exists before logging
            self.logger.log_event(f"{self.name} brightness set to {self.brightness}.")

    def set_color(self, color):
        self.color = color
        print(f"{self.name} color set to {self.color}.")
        if self.logger:  # Check if logger exists before logging
            self.logger.log_event(f"{self.name} color set to {self.color}.")

    def get_status(self):
        status = super().get_status()
        return f"{status}, Brightness: {self.brightness}, Color: {self.color}"
