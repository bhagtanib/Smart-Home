class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    def log_event(self, event):
        with open(self.log_file, 'a') as f:
            f.write(event + '\n')

    def get_logs(self):
        with open(self.log_file, 'r') as f:
            return f.read()

