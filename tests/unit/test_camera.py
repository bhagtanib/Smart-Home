import unittest
from devices.camera import Camera

class TestCamera(unittest.TestCase):
    def setUp(self):
        self.camera = Camera(device_id=1, name="Test Camera", location="Living Room")

    def test_initial_state(self):
        self.assertEqual(self.camera.get_status(), "off, Recording: False, Location: Living Room")

    def test_start_recording(self):
        self.camera.start_recording()
        self.assertEqual(self.camera.get_status(), "off, Recording: True, Location: Living Room")

    def test_stop_recording(self):
        self.camera.start_recording()
        self.camera.stop_recording()
        self.assertEqual(self.camera.get_status(), "off, Recording: False, Location: Living Room")

if __name__ == '__main__':
    unittest.main()
