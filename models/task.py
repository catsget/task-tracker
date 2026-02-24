import random
from datetime import datetime
import storage


def generate_unique_id():
    existing_ids = {task.id for task in storage.tasks}

    while True:
        new_id = random.randint(100, 999)
        if new_id not in existing_ids:
            return str(new_id)


def get_date():
    return datetime.now().isoformat()


class Task:
    def __init__(self, name: str, description: str, status=None, id=None, createdAt=None, updatedAt=None):
        if id:
            self.id = id
        else:
            self.id = generate_unique_id()
        self.name = name
        self.description = description
        self.status = status if status is not None else "todo"

        if createdAt is not None:
            self.createdAt = createdAt
        else:
            self.createdAt = get_date()

        if updatedAt is not None:
            self.updatedAt = updatedAt
        else:
            self.updatedAt = self.createdAt

    def mark_done(self):
        self.status = "done"

    def mark_in_progress(self):
        self.status = "in-progress"

    def update_name(self, name):
        self.name = name
        self.updatedAt = get_date()

    def update_desc(self, desc):
        self.description = desc
        self.updatedAt = get_date()
