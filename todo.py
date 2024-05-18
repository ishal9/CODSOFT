class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
        except IndexError:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")

        option = input("Enter an option: ")
        if option == "1":
            task = input("Enter a task to add: ")
            todo_list.add_task(task)
        elif option == "2":
            todo_list.view_tasks()
        elif option == "3":
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif option == "4":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
