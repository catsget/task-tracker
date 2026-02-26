import storage
from models import Task

def sanitize(text: str):
    return text.encode("utf-8", "ignore").decode("utf-8")

def add_task(name: str, description: str):
    safe_name = sanitize(name)
    safe_desc = sanitize(description)

    if safe_name:
        newTask = Task(name=safe_name, description=safe_desc)
        storage.tasks.append(newTask)
        storage.save_tasks()
        print(f"Task added successfully (ID: {newTask.id})")
    else:
        print("Task name is required")