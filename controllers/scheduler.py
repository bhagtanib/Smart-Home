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
        for task in list(self.tasks):
            print(f"Running task: {task}")
            self.remove_task(task)
            # Simulate task execution
            if self.logger:
                self.logger.log_event(f"Task '{task}' executed.")
