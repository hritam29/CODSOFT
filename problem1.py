import os
import json

# Function to load tasks from a file
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return {}

# Function to save tasks to a file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Function to display the To-Do List
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for task_id, task_description in tasks.items():
            print(f"{task_id}. {task_description}")

# Function to add a new task
def add_task(tasks, task_description):
    task_id = len(tasks) + 1
    tasks[task_id] = task_description
    print(f"Task '{task_description}' added with ID {task_id}.")
    save_tasks(tasks)

# Function to delete a task
def delete_task(tasks, task_id):
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task}' with ID {task_id} deleted.")
        save_tasks(tasks)
    else:
        print(f"No task found with ID {task_id}.")

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\nMenu:")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            task_description = input("Enter task description: ")
            add_task(tasks, task_description)
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(tasks, task_id)
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
