import storage

def list_tasks(status_filter=None):
    if not storage.tasks:
        print("No tasks found")
        return
    
    tasks_to_show = storage.tasks
    if status_filter:
        tasks_to_show = [task for task in storage.tasks if task.status == status_filter]
    
    if tasks_to_show:
        for task in tasks_to_show:
            print(f"{task.name} (ID: {task.id}) {task.status}")
    else:
        print(f"No tasks found with status {status_filter}")