from Startfunc import separator
import time
import random

def go_landlord():
    time.sleep(2)
    print("You meet a rich Landlord who offers you a mysterious quest. 🎩")
    time.sleep(2)

    try:
        choice = int(input('''\n🧠 Do You Want To Accept The Quest?

  >>  1. Yes
  >>  2. No

 Your Choice: '''))
    except ValueError:
        print("\n❌ Invalid input! Please enter a number (1 or 2).")
        return

    separator()
    print("You are opening the Quest... 🗃️")
    time.sleep(3)

    if choice == 1:
        step = random.choice([1, 2])
        if step == 1:
            print("🎉 Congratulations! You found gold and jewels inside the quest box.")
            separator()
            print("You Win 💰")
        else:
            print("😱 Oh No! It was a trap.\nThere was a snake inside the box, and it bit you. 🐍")
            separator()
            print("You Lose 💀")

    elif choice == 2:
        print("\n😐 You politely refuse the quest.")
        time.sleep(2)
        step = random.choice([1, 2])
        if step == 1:
            print("👑 Impressed by your honesty, the Landlord gifts you 100 acres of land! 🌾")
            separator()
            print("You Win 🏆")
        else:
            print("😡 The Landlord gets angry and thinks you're disrespecting him.\nHe pulls out a gun and shoots you! 🔫")
            separator()
            print("You Lose 💔")

    else:
        print("❌ Invalid choice! Please enter either 1 or 2.")

def go_farm():
    time.sleep(2)
    print("You see a huge Farm full of crops and animals.\n")
    print(''' ⇄ 🔒 Choose What You Want To Do On Farm:

  >>  1. Farming (Crops)         --> Press 1
  >>  2. Animal Care (Dairy)     --> Press 2
    ''')

    try:
        choice = int(input(">> Enter Your Choice: "))
    except ValueError:
        print("Invalid input! Please enter a number (1 or 2).")
        return

    separator()

    if choice == 1:
        print("🌾 You start farming... Preparing soil, sowing seeds, watering crops.")
        time.sleep(3)
        print("Waiting for crop yield...")
        time.sleep(3)
        outcome = random.choice(["good", "bad"])
        if outcome == "good":
            print("✅ Good News! You got a Great Harvest with High Yield! Farmers celebrate your success! 🎉")
            separator()
            print("You Win 🌾")
        else:
            print("❌ Bad Luck! Unexpected weather ruined your crops. It's a Bad Yield. 😞")
            separator()
            print("You Lose 🌧️")

    elif choice == 2:
        print("🐄 You head towards the barn and start caring for the animals — feeding and milking.")
        time.sleep(3)
        print("Observing animal health...")
        time.sleep(3)
        outcome = random.choice(["good", "bad"])
        if outcome == "good":
            print("✅ Excellent! Your cows gave a high-quality dairy product. The village is praising you! 🥛")
            separator()
            print("You Win 🐄")
        else:
            print("❌ Oh No! A disease spread and your animals died. Heavy Loss. 🐑💀")
            separator()
            print("You Lose 💔")
    else:
        print("Invalid choice! Please enter 1 or 2.")
def go_temple():
    time.sleep(2)
    print("You enter a peaceful Temple. Incense burns and bells ring in the distance. 🛕✨")
    time.sleep(2)

    try:
        choice = int(input('''\nWhat do you want to do?

  >>  1. Give Charity 💰
  >>  2. Eat Prasad 🍛

 Your Choice: '''))
    except ValueError:
        print("❌ Invalid input. Please enter a number (1 or 2).")
        return

    separator()
    time.sleep(3)

    if choice == 1:
        outcome = random.choice(["needy", "fraud"])
        if outcome == "needy":
            print("😊 Your donation helped someone truly in need. Good karma earned!")
            separator()
            print("You Win 🏆")
        else:
            print("😞 Your donation went to a fraud. You were tricked.")
            separator()
            print("You Lose ❌")

    elif choice == 2:
        outcome = random.choice(["fresh", "stale"])
        if outcome == "fresh":
            print("😋 The prasad was warm, sweet and satisfying. You feel blessed.")
            separator()
            print("You Win 🌟")
        else:
            print("🤢 The prasad was stale and made your stomach upset.")
            separator()
            print("You Lose 💀")

    else:
        print("❌ Invalid choice! Please choose either 1 or 2.")
def go_well():
    time.sleep(2)
    print("You arrive at an old village well. It's deep, dark, and mysterious. 💧")
    time.sleep(2)

    try:
        choice = int(input('''\nWhat do you want to do?

  >>  1. Drink water from the well 🚰
  >>  2. Don’t drink the water 🙅‍♂️

 Your Choice: '''))
    except ValueError:
        print("❌ Invalid input. Please enter a number (1 or 2).")
        return

    separator()
    time.sleep(3)

    if choice == 1:
        outcome = random.choice(["refreshed", "fell"])
        if outcome == "refreshed":
            print("✅ The water was fresh and cold. You feel energized!")
            separator()
            print("You Win 🏆")
        else:
            print("😱 You slipped while drinking and fell into the well!")
            separator()
            print("You Lose 💀")

    elif choice == 2:
        outcome = random.choice(["thirst", "poison_avoided"])
        if outcome == "thirst":
            print("🥵 You avoided drinking, but died of thirst later.")
            separator()
            print("You Lose ❌")
        else:
            print("😌 You wisely avoided the well. Turns out the water was poisoned.")
            separator()
            print("You Win 🛡️")

    else:
        print("❌ Invalid choice! Please choose either 1 or 2.")
def go_market():
    time.sleep(2)
    print("You enter the busy village market, full of colorful stalls and shouting vendors. 🏪🧺")
    time.sleep(2)

    try:
        choice = int(input('''\nWhat do you want to do?

  >>  1. Do Shopping 🛍️
  >>  2. Don’t Shop 🙅‍♂️

 Your Choice: '''))
    except ValueError:
        print("❌ Invalid input. Please enter a number (1 or 2).")
        return

    separator()
    time.sleep(3)

    if choice == 1:
        outcome = random.choice(["fair_price", "got_robbed"])
        if outcome == "fair_price":
            print("😊 You bought useful items at a fair price. Wise purchase!")
            separator()
            print("You Win 🏆")
        else:
            print("😤 The vendor fooled you with fake goods and high prices!")
            separator()
            print("You Lose ❌")

    elif choice == 2:
        outcome = random.choice(["pickpocket", "avoided_fraud"])
        if outcome == "pickpocket":
            print("😓 You didn’t shop, but someone picked your pocket in the crowd!")
            separator()
            print("You Lose 💀")
        else:
            print("😌 You noticed fraud all around and smartly walked away.")
            separator()
            print("You Win 🛡️")

    else:
        print("❌ Invalid choice! Please choose either 1 or 2.")

def go_random_in_village():
    step = random.choice([1, 2, 3, 4, 5])
    print("Teleporting To Random Location........")
    time.sleep(2)
    if step == 1:
        print(" >> (Randomly) 🔓 You Entered Landlord House")
        go_landlord()
    elif step == 2:
        print(" >> (Randomly) 🔓 You Entered Farm")
        go_farm()
    elif step == 3:
        print(" >> (Randomly) 🔓 You Entered Temple")
        go_temple()
    elif step == 4:
        print(" >> (Randomly) 🔓 You Reached Near Village Well")
        go_well()
    elif step == 5:
        print(" >> (Randomly) 🔓 You Entered Village Market")
        go_market()
def go_village():
    print("Entering Village........")
    time.sleep(2)
    print("")
    print(" >> 🔓 You Entered Village")
    time.sleep(0.5)
    print("🏙️ You step into the greenish Village — old houses, pure air and fields all around.")
    time.sleep(5)
    print("")
    print(''' ⇄ 🔒 You Have Five Places To Visit:

  >>  1. Landlord House         --> Press 1
  >>  2. Farm                   --> Press 2
  >>  3. Temple                 --> Press 3
  >>  4. Village Well           --> Press 4
  >>  5. Village Market         --> Press 5
  >>  6. Random                 --> Press 6
    ''')
    choices_village = {
        1: go_landlord,
        2: go_farm,
        3: go_temple,
        4: go_well,
        5: go_market,
        6: go_random_in_village
    }
    try:
        choice = int(input(">> Enter Your Choice: "))
        if choice in choices_village:
            separator()
            choices_village[choice]()
        else:
            print("❌ Invalid choice!")
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")