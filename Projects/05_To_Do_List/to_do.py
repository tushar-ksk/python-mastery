
def main_menu():
    menu = input("\nBack To Menu?(Y/N)>> ")
    if menu.lower() == "y":
        print("")
        print("\nYou entered Main Menu\n")
        start()
    elif menu.lower() == "n":
        print("Good Bye")
        exit()
    else:
        print("Invalid Input\nExiting Program....")
        exit()



def add_task():
    task = input("\nEnter the task >> ")
    with open('file.txt', 'r') as f:
        tasks = f.readlines()
    
    if task.lower() in str(tasks).lower():
        print("Task already added")
    
    else:        
        with open('file.txt', 'a') as f:
            f.write(f"{task}\n")
            print("\nTask Added Successfully")


def view_tasks():
    with open('file.txt', 'r') as f:
        for index, item in enumerate(f):
             print(f"\n{index+1}. {item.strip()}")


def delete_task():
    view_tasks()
    task_no = int(input("\nEnter task number to delete corresponding task: "))
    try:
        with open('file.txt', 'r') as f:
            lines = f.readlines()
            del lines[task_no-1]
        with open('file.txt', 'w') as f:
            f.writelines(lines)
            print("\nTask removed successfully")
    except ValueError as e:
        print(e)




## To do list

print("\n~~~~~~~~You entered TO DO list~~~~~~~~~\n")
def start():

        
    while True:
        
        print('''1. Add task
2. View task
3. Delete task''')
        options = {
            1 : add_task ,
            2 : view_tasks,
            3 : delete_task

        }
        try:
            choice = int(input("Enter Your Choice: "))
            try:
                if choice in options:
                    options.get(choice)()
                    main_menu()
                else:
                    print("Invlid Input")
            except KeyError as e:
                print(e)
        except ValueError as e:
            print(f"\nError: {e}\n")
            print("\n~~~~~~~~You entered TO DO list~~~~~~~~~\n")
            
start()