# Todo List Application

# Function to display the menu options
def display_menu():
    print("Todo List Menu:")
    print("1. View Todo List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

# Function to view the todo list
def view_todo_list(todo_list):
    if len(todo_list) == 0:
        print("Todo list is empty.")
    else:
        print("Todo List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to add a task to the todo list
def add_task(todo_list):
    task = input("Enter task: ")
    todo_list.append(task)
    print("Task added successfully.")

# Function to mark a task as completed
def mark_completed(todo_list):
    view_todo_list(todo_list)
    task_number = int(input("Enter the task number to mark as completed: "))
    if task_number >= 1 and task_number <= len(todo_list):
        task = todo_list[task_number - 1]
        print(f"Marked task '{task}' as completed.")
        todo_list.remove(task)
    else:
        print("Invalid task number.")

# Function to delete a task from the todo list
def delete_task(todo_list):
    view_todo_list(todo_list)
    task_number = int(input("Enter the task number to delete: "))
    if task_number >= 1 and task_number <= len(todo_list):
        task = todo_list[task_number - 1]
        todo_list.remove(task)
        print(f"Deleted task '{task}'.")
    else:
        print("Invalid task number.")

# Main function
def main():
    todo_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            view_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            mark_completed(todo_list)
        elif choice == "4":
            delete_task(todo_list)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
