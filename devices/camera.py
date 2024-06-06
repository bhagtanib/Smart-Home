from devices.device import Device
class Camera(Device):
    def __init__(self, device_id, name, location, logger=None):
        super().__init__(device_id, name, logger=logger)
        self.recording = False
        self.location = location
    
    def start_recording(self):
        self.recording = True
        print(f"{self.name} started recording.")
    
    def stop_recording(self):
        self.recording = False
        print(f"{self.name} stopped recording.")
    
    def get_feed(self):
        if self.recording:
            return f"{self.name} is recording at {self.location}."
        else:
            return f"{self.name} is not recording."
    
    def get_status(self):
        status = super().get_status()
        return f"{status}, Recording: {self.recording}, Location: {self.location}"
