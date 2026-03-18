# Patient model for storing patient data
from datetime import datetime

class Patient:
    def __init__(self, name):
        self.name = name
        self.arrival_time = datetime.now()

    def get_details(self):
        return f"{self.name} arrived at {self.arrival_time}"