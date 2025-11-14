def load_tasks():
    tasks = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 4:
                    tasks.append({
                        "task": parts[0],
                        "priority": parts[1],
                        "due": parts[2],
                        "done": parts[3] == "1"
                    })
    except FileNotFoundError:
        pass
    return tasks
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for t in tasks:
            done_flag = "1" if t["done"] else "0"
            file.write(f"{t['task']} | {t['priority']} | {t['due']} | {done_flag}\n")
def add_task(tasks):
    task = input("Enter task: ")
    priority = input("Priority (Low/Medium/High): ").capitalize()
    due = input("Due date (optional): ")
    tasks.append({"task": task, "priority": priority, "due": due, "done": False})
    save_tasks(tasks)
    print("Task added!\n")
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.\n")
        return
    print("\n--- Tasks ---")
    for i, t in enumerate(tasks, 1):
        status = "✔" if t["done"] else "✗"
        due_display = t["due"] if t["due"] else "No due date"
        print(f"{i}. {t['task']}  [{t['priority']}]  (Due: {due_display})  Status: {status}")
    print()
def mark_complete(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark complete: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Marked as complete!\n")
    except:
        print("Invalid choice.\n")
def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['task']}\n")
    except:
        print("Invalid choice.\n")
def main():
    tasks = load_tasks()
    while True:
        print("=== SIMPLE TO-DO APP ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task complete")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")

