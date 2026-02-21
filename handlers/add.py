import storage
from models import Task

def add_task(name: str, description: str):
    if name:
        newTask = Task(name=name, description=description)
        storage.tasks.append(newTask)
        storage.save_tasks()
        print(f"Task added successfully (ID: {newTask.id})")
