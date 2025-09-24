import sys
import sys
import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(task):
    if not task.strip():
        print("Cannot add an empty task.")
        return
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})  # зберігаємо словник
    save_tasks(tasks)
    print(f"Added: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✔" if t["done"] else "✘"
        print(f"{i}. {t['task']} [{status}]")

def mark_done(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index-1]["done"] = True
        save_tasks(tasks)
        print(f"Marked as done: {tasks[index-1]['task']}")
    else:
        print("Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index-1)
        save_tasks(tasks)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid task number.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python todo.py [add/list/done/delete]")
    elif sys.argv[1] == "add":
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_tasks()
    elif sys.argv[1] == "done":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("Usage: python todo.py done [task_number]")
        else:
            mark_done(int(sys.argv[2]))
    elif sys.argv[1] == "delete":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("Usage: python todo.py delete [task_number]")
        else:
            delete_task(int(sys.argv[2]))


