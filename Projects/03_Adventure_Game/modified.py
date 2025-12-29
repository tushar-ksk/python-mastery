# Adventure Game
import time
from village import go_village
from town import go_town
from forest import go_forest
from randomstart import Random_Start


print("\n\nGame starting...\n")


def separator(n = 1):
    print("-"*147*n)
    print("")


def start():
    time.sleep(1)
    print("                                    >>>>>  ~You Found Yourself At A Town Roundabout Crossroads~   <<<<<")
    separator(2)
    time.sleep(2)
    print(''' ⇄ 🔒 You Have Four Path To Move:

>>  1. Village       --> Press 1
>>  2. Town          --> Press 2
>>  3. Forest        --> Press 3
>>  4. Random        --> Press 4          ''')
   
    choices_map = {
        1 : go_village,
        2 : go_town,
        3 : go_forest,
        4 : Random_Start
    }

    print("")
    time.sleep(1)
    choice = int(input("Enter You Choice: "))
    separator()

    try:
        if choice in choices_map:
            choices_map[choice]()
        else:
            print("invalid choice")
    
    except ValueError:
        print("Invalid Input! Please enter a valid input")


start()