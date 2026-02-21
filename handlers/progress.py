import storage


def mark_in_progress(id: str):
    if id:
        selectedTask = None
        for task in storage.tasks:
            if task.id == id:
                selectedTask = task

        if not selectedTask:
            print("Task marked in-progress unsuccessfully. Check your ID")
            return

        selectedTask.mark_in_progress()
        storage.save_tasks()
        print(f"Task marked in-progress successfully (ID: {selectedTask.id})")
