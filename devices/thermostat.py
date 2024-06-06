from devices.device import Device

class Thermostat(Device):
    def __init__(self, device_id, name, current_temperature=20, target_temperature=22, logger=None):
        super().__init__(device_id, name, logger=logger)
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature
    
    def set_temperature(self, temp):
        self.target_temperature = temp
        print(f"{self.name} target temperature set to {self.target_temperature}.")
        if self.logger:  # Check if logger exists before logging
            self.logger.log_event(f"{self.name} target temperature set to {self.target_temperature}.")

    def get_current_temperature(self):
        return self.current_temperature
    
    def get_status(self):
        status = super().get_status()
        return f"{status}, Current Temperature: {self.current_temperature}, Target Temperature: {self.target_temperature}"
