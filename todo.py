tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # of the task you want to delete: "))
        if 0 <= taskToDelete < len(tasks):
            removed_task = tasks.pop(taskToDelete)
            print(f"Task '{removed_task}' has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    print("Welcome to the to-do list app :)")
    while True:
        print("\n")
        print("Please select one of the following options:")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid input. Please try again.")
