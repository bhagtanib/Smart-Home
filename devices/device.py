class Device:
    def __init__(self, device_id, name, logger=None):  # Add logger parameter
        self.device_id = device_id
        self.name = name
        self.status = 'off'
        self.logger = logger  # Assign logger instance
    
    def turn_on(self):
        self.status = 'on'
        print(f"{self.name} is now ON.")
        if self.logger:  # Check if logger exists before logging
            self.logger.log_event(f"{self.name} is now ON.")

    def turn_off(self):
        self.status = 'off'
        print(f"{self.name} is now OFF.")
        if self.logger:  # Check if logger exists before logging
            self.logger.log_event(f"{self.name} is now OFF.")

    def get_status(self):
        return self.status
