todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("Your tasks:")
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task}")

def remove_task(task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task index.")

while True:
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_index = int(input("Enter the task index to remove: "))
        remove_task(task_index)
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
