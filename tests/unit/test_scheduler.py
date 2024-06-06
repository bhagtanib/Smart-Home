import unittest
from controllers.scheduler import Scheduler

class TestScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = Scheduler()

    def test_schedule_task(self):
        self.scheduler.schedule_task("Turn off living room light at 10:00 PM")
        self.assertIn("Turn off living room light at 10:00 PM", self.scheduler.tasks)

    def test_run_tasks(self):
        self.scheduler.schedule_task("Task 1")
        self.scheduler.schedule_task("Task 2")
        self.scheduler.schedule_task("Task 3")
        self.scheduler.schedule_task("Task 4")
        self.scheduler.schedule_task("Task 5")
        self.scheduler.run_tasks()
        self.assertEqual(self.scheduler.tasks, [])

if __name__ == '__main__':
    unittest.main()
