import storage


def update_task_desc(id: str, new_desc: str):
    if id and new_desc:
        selected_task = None
        for task in storage.tasks:
            if task.id == id:
                selected_task = task
                break

        if not selected_task:
            print("Task not found")
            return

        selected_task.update_desc(new_desc)
        storage.save_tasks()
        print(f"Task updated successfully (ID: {selected_task.id})")
        return
    else:
        print("Check ID and Description")
