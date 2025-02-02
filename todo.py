tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added ")
    
def view_task():
    if not tasks:
        print("No task founded")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

task1 = input("Enter a task to add in the list")
add_task(task1)


show =view_task()

print(show)


