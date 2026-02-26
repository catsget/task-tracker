import sys
import storage
from handlers import *

def show_usage():
    print("""
    Usage: task-tracker <command> [arguments]
    
    Commands:
        add <name> [desc]
        list [status]
        show <id>
        delete <id>
        update <id> <new name>
        update-desc <id> <new desc>
        mark-done <id>
        mark-in-progress <id>
    """)


def main(operation: str, arg, arg2):
    storage.load_tasks()

    commands = {
        "add": lambda: add_task(arg, arg2),
        "list": lambda: list_tasks(arg),
        "show": lambda: show_task(arg),
        "delete": lambda: delete_task(arg),
        "update": lambda: update_task(arg, arg2),
        "update-desc": lambda: update_task_desc(arg, arg2),
        "mark-done": lambda: mark_done(arg),
        "mark-in-progress": lambda: mark_in_progress(arg)
    }

    if operation in commands:
        commands[operation]()
    else:
        print(f"Unknown command: {operation}")
        show_usage()


if __name__ == "__main__":
    try:
        operation = sys.argv[1]

        arg = sys.argv[2] if len(sys.argv) > 2 else ""
        arg2 = sys.argv[3] if len(sys.argv) > 3 else ""
        main(operation, arg, arg2)
    except IndexError:
        show_usage()
