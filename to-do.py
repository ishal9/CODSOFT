tasks = []
def display_menu():
    print("To-Do List Application")
    print("======================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter the task description: ")
    tasks.append({"description": task})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks):
        status = "Pending"
        print(f"{idx + 1}. {task['description']}")


def delete_task():
    view_tasks()
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
            input("Press Enter to continue...")
        elif choice == '3':
            delete_task()
            input("Press Enter to continue...")
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
