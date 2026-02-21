import json
import os
from utils.converter import to_dict, to_object

tasks = None


def save_tasks():
    global tasks

    os.makedirs("storage", exist_ok=True)

    with open("storage/tasks.json", "w", encoding="utf-8") as f:
        json.dump([to_dict(t) for t in tasks], f, ensure_ascii=False, indent=2, default=str)


def load_tasks():
    global tasks

    try:
        with open("storage/tasks.json", "r", encoding="utf-8") as f:
            tasks = []

            for task in json.load(f):
                tasks.append(to_object(task))
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
