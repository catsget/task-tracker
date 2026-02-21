import random
from datetime import datetime
import storage

def generate_unique_id():
    existing_ids = {task.id for task in storage.tasks}

    while True:
        new_id = random.randint(100, 999)
        if new_id not in existing_ids:
            return str(new_id)

class Task:
    def __init__(self, name: str, description: str, status=None, id=None, createdAt=None):
        if id:
            self.id = id
        else:
            self.id = generate_unique_id()
        self.name = name
        self.description = description
        self.status = status if status else "todo"


    def mark_done(self):
        self.status = "done"

    def mark_in_progress(self):
        self.status = "in-progress"