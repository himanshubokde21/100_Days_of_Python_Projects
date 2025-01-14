def task():
    tasks = [ ] # empty tasks
    print("""
        1. type "add" to add new task.
        2. type "view" to view all tasks.
        3. type "del" to delete task.
        4. type "close" to close app.
        """) # Instructions 
    msg = input("Enter your Message : ") #user input
    while True:
        if msg == "add": 
            ele = input("Enter your task : ")
            tasks.append(ele)
            print("your task is added\n")
            msg = input("Whats next : ")
            
        elif msg == "view": 
            if not tasks:
                print("no task to view\n")
                msg = input("whats next : ")
                continue 
            for t, task in enumerate(tasks):
                print(f"task {t+1} - {task}")
            print(f"Total Tasks {len(tasks)}\n")
            msg = input("whats next : ")
            
        elif msg == "del":
            if not tasks:
                print("no task to delete\n")
                msg = input("whats next : ")
                continue 
            size = [x for x in range(1, len(tasks)+1)]
            while True:
                index = int(input("Enter Task Number : "))
                if index in size:
                     tasks.pop(index-1)
                     print(f"Task {index } is Successfully Deleted\n")
                     msg = input("whats next : ")
                     break
                else:
                     print("Wrong Task Number\n")
                     msg = input("whats next : ")
                     continue 
                 
        elif msg == "close": 
            print("Thanks for using these app")
            break
         
        else: 
            print("Wrong Message\n")
            msg = input("whats next : ")
            
print("Welcome to 'To Do App' ")
task()
