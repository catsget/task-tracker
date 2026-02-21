import storage

def delete_task(id: str):
    if not storage.tasks:
        print("No tasks found")
        return
    selectedTask = None
    for task in storage.tasks:
        if task.id == id:
            selectedTask = task
            break

    if not selectedTask:
        print("Task deleted unsuccessfully. Check your ID")
        return

    confirm = input("Are you sure? y or n: ")

    if confirm.lower() == "y":
        storage.tasks.pop(storage.tasks.index(selectedTask))
        storage.save_tasks()
        print(f"Task deleted successfully (ID: {selectedTask.id})")
        return
    else:
        print("Aborting...")
        return