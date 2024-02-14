class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def update_task(self, index, new_task):
        if index >= 0 and index < len(self.tasks):
            self.tasks[index] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid index.")

    def delete_task(self, index):
        if index >= 0 and index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted successfully!")
        else:
            print("Invalid index.")

    def show_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
        else:
            print("Your To-Do List is empty.")


def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Show Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter the index of task to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(index, new_task)
        elif choice == '3':
            index = int(input("Enter the index of task to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '4':
            todo_list.show_tasks()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
