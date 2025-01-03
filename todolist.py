def task():
    tasks=[]
    print("_______TO DO LIST_______")
    no_of_tasks=int(input("ENTER NUMBER OF TASKS:"))
    for i in range (1,no_of_tasks+1):
        task_name=input(f"ENTER TASK {i}:")
        tasks.append(task_name)
    print("TASKS:")
    print(tasks)
    while True:
        operations=int(input("Enter 1 to Add task\nEnter 2 to Update task\nEnter 3 to Delete task\nEnter 4 to View the task\nEnter 5 to Exit  " ))
        if operations==1:
            print("_______ADD THE TASK_______")
            add=input("Enter the task to be added:")
            tasks.append(add)
            print(tasks)
        elif operations==2:
            print("_______UPDATE THE TASK_______")
            update_task=input("Enter the task to be updated:")
            if update_task in tasks:
                new_task=input("Enter new task:")
                ind=tasks.index(update_task)
                tasks[ind]=new_task
                print(tasks)
        elif operations==3:
            print("________DELETE THE TASK_______")
            delete_task=input("Enter the task to be deleted:")
            if delete_task in tasks:
                ind=tasks.index(delete_task)
                del tasks[ind]
            print(tasks)
        elif operations==4:
            print("_______VIEW THE TASK_______")
            print(tasks)
        elif operations==5:
            print("_______EXIT THE PROGRAM_______")
            break
        else:
            print("_______Invalid Input_______")
            break;

task()

