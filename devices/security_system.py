from devices.device import Device

class SecuritySystem(Device):
    def __init__(self, device_id, name, logger=None):
        super().__init__(device_id, name, logger=logger)
        self.armed = False
        self.sensors = []
    
    def arm(self):
        self.armed = True
        print(f"{self.name} is now ARMED.")
        if self.logger:  # Check if logger exists before logging
            self.logger.log_event(f"{self.name} is now ARMED.")

    def disarm(self):
        self.armed = False
        print(f"{self.name} is now DISARMED.")
        if self.logger:  # Check if logger exists before logging
            self.logger.log_event(f"{self.name} is now DISARMED.")

    def add_sensor(self, sensor):
        self.sensors.append(sensor)
        print(f"Sensor {sensor} added to {self.name}.")
        if self.logger:  # Check if logger exists before logging
            self.logger.log_event(f"Sensor {sensor} added to {self.name}.")

    def get_status(self):
        status = super().get_status()
        return f"{status}, Armed: {self.armed}, Sensors: {self.sensors}"
