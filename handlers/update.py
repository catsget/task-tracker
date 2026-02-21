import storage

def update_task(id: str, newName: str):
    if id and newName:
        selectedTask = None
        for task in storage.tasks:
            if task.id == id:
                selectedTask = task
                break
        
        if not selectedTask:
            print("Task updated unsuccessfully. Check your ID")
            return
        
        selectedTask.name = newName
        storage.save_tasks()
        print(f"Task updated successfully (ID: {selectedTask.id})")
        return