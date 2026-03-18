# Handles queue operations like add and serve patient
from models import Patient

class ClinicQueue:
    def __init__(self):
        self.queue = []
        self.served_today = 0

    def add_patient(self, name):
        patient = Patient(name)
        self.queue.append(patient)

    def serve_patient(self):
        if self.queue:
            served = self.queue.pop(0)
            self.served_today += 1
            return served

    def get_queue(self):
        return self.queue