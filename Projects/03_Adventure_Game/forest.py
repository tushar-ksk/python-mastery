from Startfunc import separator
import time
import random

def go_cave():
    print("\nYou light a torch and enter the damp, echoing cave.")
    time.sleep(2)

    try:
        choice = int(input('''\nWhat do you want to do?

  >>  1. Search for treasure 💰
  >>  2. Follow the echoing sound 🎧

 Your Choice: '''))
    except ValueError:
        print("❌ Invalid input.")
        return

    separator()
    time.sleep(3)

    if choice == 1:
        outcome = random.choice(["gold", "snake"])
        if outcome == "gold":
            print("🪙 You found an ancient gold chest!")
            print("You Win 🏆")
        else:
            print("🐍 A snake jumped out of the dark!")
            print("You Lose 💀")
    elif choice == 2:
        outcome = random.choice(["mystic", "collapse"])
        if outcome == "mystic":
            print("🧝‍♂️ A forest spirit blessed you for bravery.")
            print("You Win 🏆")
        else:
            print("🪨 The cave collapsed behind you. No way out.")
            print("You Lose 💀")
    else:
        print("❌ Invalid choice!")

def go_old_tree():
    print("\nYou approach a gigantic ancient tree with twisted roots and carvings.")
    time.sleep(2)

    try:
        choice = int(input('''\nWhat do you want to do?

  >>  1. Knock on the trunk 🔔
  >>  2. Climb the tree 🧗

 Your Choice: '''))
    except ValueError:
        print("❌ Invalid input.")
        return

    separator()
    time.sleep(3)

    if choice == 1:
        outcome = random.choice(["open", "curse"])
        if outcome == "open":
            print("🌟 A secret door opened revealing a hidden scroll!")
            print("You Win 🏆")
        else:
            print("💀 The tree cursed you for disturbing its sleep.")
            print("You Lose 👻")
    elif choice == 2:
        outcome = random.choice(["fruit", "fall"])
        if outcome == "fruit":
            print("🍎 You found a glowing fruit that boosts energy.")
            print("You Win 🏆")
        else:
            print("😵 You slipped and fell hard from the top!")
            print("You Lose 💀")
    else:
        print("❌ Invalid choice!")
def go_hunting_zone():
    print("\nYou see fresh paw marks. A predator might be nearby...")
    time.sleep(2)

    try:
        choice = int(input('''\nWhat do you want to do?

  >>  1. Hide behind bushes 🌿
  >>  2. Try hunting an animal 🏹

 Your Choice: '''))
    except ValueError:
        print("❌ Invalid input.")
        return

    separator()
    time.sleep(3)

    if choice == 1:
        outcome = random.choice(["safe", "caught"])
        if outcome == "safe":
            print("🤫 The tiger passed by. You survived!")
            print("You Win 🏆")
        else:
            print("🦁 The beast smelled you and attacked!")
            print("You Lose 💀")
    elif choice == 2:
        outcome = random.choice(["deer", "backfire"])
        if outcome == "deer":
            print("🏹 You hunted a deer successfully!")
            print("You Win 🏆")
        else:
            print("🔫 Your weapon backfired and injured you.")
            print("You Lose 💀")
    else:
        print("❌ Invalid choice!")
def go_herbal_hut():
    print("\nYou reach a hut made of leaves. A herbalist greets you.")
    time.sleep(2)

    try:
        choice = int(input('''\nWhat do you want to do?

  >>  1. Ask for a healing potion 🧪
  >>  2. Drink from the mystery bottle 🫗

 Your Choice: '''))
    except ValueError:
        print("❌ Invalid input.")
        return

    separator()
    time.sleep(3)

    if choice == 1:
        outcome = random.choice(["healed", "expired"])
        if outcome == "healed":
            print("💚 Your wounds are healed and energy restored!")
            print("You Win 🏆")
        else:
            print("☠️ The potion was expired. You feel dizzy...")
            print("You Lose 💀")
    elif choice == 2:
        outcome = random.choice(["superpowers", "poison"])
        if outcome == "superpowers":
            print("⚡ You feel strength and speed surge through you!")
            print("You Win 🏆")
        else:
            print("💀 The bottle was poison. You collapse!")
            print("You Lose 💀")
    else:
        print("❌ Invalid choice!")
def go_waterfall():
    print("\nYou stand before a majestic Waterfall, misty air and roaring sound fills your ears.")
    time.sleep(2)

    try:
        choice = int(input('''\nWhat do you want to do?

  >>  1. Dive into the pool 🌊
  >>  2. Climb behind the waterfall 🧗‍♂️

 Your Choice: '''))
    except ValueError:
        print("❌ Invalid input.")
        return

    separator()
    time.sleep(3)

    if choice == 1:
        outcome = random.choice(["treasure", "rocks"])
        if outcome == "treasure":
            print("💰 You discover a chest hidden underwater with gold coins!")
            print("You Win 🏆")
        else:
            print("🪨 You hit sharp rocks under water!")
            print("You Lose 💀")
    elif choice == 2:
        outcome = random.choice(["hidden cave", "slip"])
        if outcome == "hidden cave":
            print("🕳️ Behind the fall was a hidden cave full of glowing crystals!")
            print("You Win 🏆")
        else:
            print("😖 You slipped and fell down the rocky slope.")
            print("You Lose 💀")
    else:
        print("❌ Invalid choice!")
def go_random_in_forest():
    step = random.choice([1, 2, 3, 4,5])
    print("Teleporting to a random location in the Forest...")
    time.sleep(2)
    if step == 1:
        print(" >> (Randomly) 🔓 You Entered Cave")
        go_cave()
    elif step == 2:
        print(" >> (Randomly) 🔓 You Reached Near An Old Tree")
        go_old_tree()
    elif step == 3:
        print(" >> (Randomly) 🔓 You Entered Hunting Zone")
        go_hunting_zone()
    elif step == 4:
        print(" >> (Randomly) 🔓 You Entered Herbal Hut")
        go_herbal_hut()
    elif step == 5:
        print(" >> (Randomly) 🔓 You Reached Near Waterfall")
        go_waterfall()

def go_forest():
    print("Entering Forest........")
    time.sleep(2)
    print("")
    print(" >> 🔓 You Entered Forest")
    time.sleep(0.5)
    print("🌲 You step into the dark and mysterious Forest. Birds chirping, wind rustling...")
    time.sleep(5)
    print("")
    print(''' ⇄ 🌿 You Have Five Places To Visit:

  >>  1. Explore the Cave         --> Press 1
  >>  2. Inspect the Old Tree     --> Press 2
  >>  3. Enter Hunting Zone       --> Press 3
  >>  4. Visit Herbal Hut         --> Press 4
  >>  5. Explore Waterfall        --> Press 5
  >>  6. Random                   --> Press 6

    ''')

    choices_forest = {
        1: go_cave,
        2: go_old_tree,
        3: go_hunting_zone,
        4: go_herbal_hut,
        5: go_waterfall,
        6: go_random_in_forest
    }
    try:
        choice = int(input(">> Enter Your Choice: "))
        if choice in choices_forest:
            separator()
            choices_forest[choice]()
        else:
            print("❌ Invalid choice!")
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")
