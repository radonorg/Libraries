import datetime

class Timer:
    def __init__(self):
        self.seconds = 0
        self.start_time = 0
        self.stop_time = 0
    def start(self):
        self.start_time = datetime.time()
    def stop(self):
        self.stop_time = datetime.time()
        total_time = self.stop_time - self.start_time
        self.seconds = total_time
    def get(self):
        return self.seconds