import storage

def show_task(id: str):
    if storage.tasks:
        selected_task = None
        for task in storage.tasks:
            if task.id == id:
                selected_task = task
                break
        
        if selected_task:
            name = selected_task.name
            desc = selected_task.description
            print(f"ID: {id}")
            print(name)
            print(desc if desc else "No description")