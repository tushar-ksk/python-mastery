
def main_menu():
    menu = input("\nEnter Yes if you want to go menu >> ")
    if menu.lower() == "yes":
        print("")
        print("\nYou entered Main Menu\n")
        return start()
    else:
        exit()



def add_task():
    task = input("\nEnter the task >> ")
    if task.lower() in [tasks.lower() for tasks in to_do]:
        print("Task already added")

    else:        
        to_do.append(task)
        to_do.sort()
        print("\nTask Added Successfully")

    main_menu()


def view_tasks():
    for index, item in enumerate(to_do):
        print(f"\n{index+1}. {item}")

    main_menu()


def delete_task():
    for index, item in enumerate(to_do):
        print(f"\n{index+1}. {item}")

    task_no = int(input("\nEnter task number to delete corresponding task"))
    to_do.pop(task_no-1)
    print("\nTask removed successfully")

    main_menu()



## To do list

to_do = []

def start():
    print("\nYou entered TO DO list\n")
        
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
                    print(options.get(choice)())
                else:
                    print("Invlid Input")
            except KeyError as e:
                print(e)
        except ValueError as e:
            print("Error:",e)
            
start()