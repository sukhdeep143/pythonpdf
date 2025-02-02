tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added ")
    
def view_tasks():
    if not tasks:
        print("No task founded")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
            


# Main program loop
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")

    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    
    


