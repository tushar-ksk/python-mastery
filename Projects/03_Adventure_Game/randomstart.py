from Startfunc import separator
import random
import time
from village import go_village
from forest import go_forest
from town import go_town


def Random_Start():
    print("Teleporting you to a random location.....")
    time.sleep(2)
    step = random.choice([1,2,3])
    separator()
    if step  == 1:
        print("")
        go_village()
    elif step == 2:
        print("")
        go_town()
    elif step == 3:
        print("")
        go_forest()