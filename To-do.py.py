tasks = []

def add_task():
    task = input("enter task: ")
    task = {"task_name": task, "done": False}
    tasks.append(task)
    print("task added!")
    
        
def show_task():
    for i, t in enumerate(tasks, start=1):
        if t["done"]:
            status = "✅" 
        else:
                status="❌"
        print(f"{i}.{t['task_name']} {status}")

def mark_complete():
    num=int(input("enter task num to be complete: "))
    tasks[num-1]["done"]=True
    print("task marked as completed.")
    
    
 
def delete():
    num=int(input("enter task num to be deleted: "))
    tasks.pop(num-1)
    
    
while True:
    print("\n1. Add Task")
    print("2. Show Task")
    print("3. marked complete")
    print("4. deletion")
    print("5. exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_task()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
         delete()
    elif choice=="5":
        break
    else:
        print("Invalid choice")
        