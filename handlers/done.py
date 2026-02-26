import storage

def mark_done(id: str):
    if id:
        selectedTask = None
        for task in storage.tasks:
            if task.id == id:
                selectedTask = task
        
        if not selectedTask:
            print("Task not found")
            return
        
        selectedTask.mark_done()
        storage.save_tasks()
        print(f"Task marked done successfully (ID: {selectedTask.id})")
    else:
        print("ID is required")