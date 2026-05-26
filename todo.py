# Task 1: To-Do List by Lakshmi
tasks = []

def show_menu():
    print("\n--- LAKSHMI'S TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks") 
    print("3. Mark Task as Done")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter choice 1-4: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added:", task)
    
    elif choice == "2":
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks yet. Add chey Lakshmi!")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
    
    elif choice == "3":
        num = int(input("Enter task number to mark done: "))
        if 1 <= num <= len(tasks):
            print("Completed:", tasks[num-1])
            tasks.pop(num-1)
        else:
            print("Wrong number Lakshmi!")
            
    elif choice == "4":
        print("Bye Lakshmi! Task-1 Complete 🔥")
        break
    
    else:
        print("1-4 madhyalo number kottu")