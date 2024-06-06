import time

class Scheduler:
    def __init__(self, logger=None):
        self.tasks = []
        self.logger = logger

    def schedule_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' scheduled.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print(f"Task '{task}' not found.")

    def run_tasks(self):
        for task in self.tasks:
            print(f"Running task: {task}")
            # Perform task execution here
            time.sleep(1)  # Simulating task execution time
