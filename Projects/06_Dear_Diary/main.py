import time
import datetime
import os


folder_path = r"C:\Users\navne\OneDrive\01_coding\python1\Projects\06_Dear_Diary\entries"

def add_entry():
    new_diary = input("Enter title for your today diary >>> ")
    file = os.path.join(folder_path,new_diary)
    with open(fr"{file}.txt", 'a+') as d:
        date = str(datetime.date.today())
        d.write(f"{date}\n")
        try:
            max_lines = int(input("Enter the number of lines you want to write: "))
            print(f"Note: Once you complete {max_lines}th line, your Diary will be autosaved.\nIf you want to save your Diary before reaching last line You can simply write 'SAVE' in new line and then press enter!")
            print("Start Writing:\n")
                
            for i in range(1,(max_lines+1)):
                line = input("")
                if line.lower() == "save":
                    break
                else:
                    d.writelines(f"\n{line}")
            d.write("\n")
            d.write("~"*147)
            d.write("\n")

        except ValueError:
            print("Invalid number. Try again.")
            return
        
    

def past_entries():
    files = os.listdir(folder_path)
    if not files:
        print("No diary entries found.")
    else:
        for index, file in enumerate(files):
            print(f"{index+1}. {file}")


def delete_entries():
    past_entries()
    try:
        diary_num = int(input("Enter the diary index number to delete: "))
        files = os.listdir(folder_path)
        file_to_delete = os.path.join(folder_path, files[diary_num-1])
        confirm = input(f"Are you sure you want to delete '{files[diary_num-1]}'? (yes/no): ")
        if confirm.lower() == "yes":
            os.remove(file_to_delete)
            print(f"{files[diary_num-1]} deleted successfully.")
        else:
            print("Deletion cancelled.")
    except (ValueError, IndexError):
        print("Invalid index number. Please try again.")
        return


print(">>>>>>> Welcome to Diary <<<<<<<")
user = input("Enter Your Name: ")
print("\nEntering Main Menu....")
time.sleep(1)
def menu():
    print("\n>>>> Main Menu")
    print(f"Hey, {user}. You can share your day with me without any hesitation.")
    print('''\nHow can i help you?\n1. Add a new entry
2. View past entries
3. Delete an entry
4. Exit
''')
    choices = {
        1 : add_entry,
        2 : past_entries,
        3 : delete_entries,
        4 : exit
    }
    try:
        user_choice = int(input("Enter Your Choice: "))
        if user_choice in choices:
            choices[user_choice]()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    except ValueError:
        print("Please enter a valid number.")


while True:
    menu()
