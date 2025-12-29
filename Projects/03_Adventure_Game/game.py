# Adventure Game
import random
import time


print("\n\nGame starting...\n")


def separator(n = 1):
    print("-"*163*n)
    print("")


def start():
    time.sleep(3)
    print("                                    >>>>>  ~You Found Yourself At A Town Roundabout Crossroads~   <<<<<")
    separator(2)
    time.sleep(2)
    print(''' ⇄ 🔒 You Have Four Path To Move:

>>  1. Village       --> Press 1
>>  2. Town          --> Press 2
>>  3. Forest        --> Press 3
>>  4. Random        --> Press 4          ''')
    choice = int(input(">> Enter Your Choice: "))
    if choice == 1:
        separator()
        print("Entering Village.....")
        time.sleep(2)
        print("")
        print(" >> 🔓 You Entered Village")
        Village()
    elif choice == 2:
        separator()
        print(" >> 🔓 You Entered Town")
    elif choice == 3:
        separator()
        print(" >> 🔓 You Entered Forest")
    elif choice == 4:
        step = random.choice([1,2,3])
        separator()
        if step  == 1:
            separator()
            print(" >> (Randomly) 🔓 You Entered Village")
        elif step == 2:
            separator()
            print(" >> (Randomly) 🔓 You Entered Town")
        elif step == 3:
            separator()
            print(" >> (Randomly) 🔓 You Entered Forest")

# Village

def Village():
    print("")
    print(''' ⇄ 🔒 You Have Five Places To Visit:

>>  1. Landlord House       --> Press 1
>>  2. Farm                 --> Press 2
>>  3. Temple               --> Press 3
>>  4. Village Well         --> Press 4
>>  5. Village Market       --> Press 5
>>  6. Random               --> Press 6
    ''')
    try:
        choice = int(input(">> Enter Your Choice: "))
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")
        return

    if choice == 1:
        separator()
        time.sleep(3)
        print("Entering Landlord House......")
        print(" >> 🔓 You Entered Landlord House")
        LandLord()
    elif choice == 2:
        separator()
        print("Entering Farm.....")
        time.sleep(2)
        print(" >> 🔓 You Entered Farm")
        Farm()
    elif choice == 3:
        separator()
        print("Entering Temple....")
        time.sleep(2)
        print(" >> 🔓 You Entered Temple")
        Temple()
    elif choice == 4:
        separator()
        print("Walking towards the Village Well...")
        time.sleep(2)
        Well()
    elif choice == 5:
        separator()
        print("Heading to the Village Market...")
        time.sleep(2)
        Market()
    elif choice == 6:
        step = random.choice([1, 2, 3, 4, 5])
        separator()
        print("Teleporting To Random Location........")
        time.sleep(2)
        if step == 1:
            print(" >> (Randomly) 🔓 You Entered Landlord House")
            LandLord()
        elif step == 2:
            print(" >> (Randomly) 🔓 You Entered Farm")
            Farm()
        elif step == 3:
            print(" >> (Randomly) 🔓 You Entered Temple")
            Temple()
        elif step == 4:
            print(" >> (Randomly) 🔓 You Entered Village Well")
            Well()
        elif step == 5:
            print(" >> (Randomly) 🔓 You Entered Village Market")
            Market()
    else:
        print("❌ Invalid choice!")

# Town

def Town():
    time.sleep(2)
    print("🏙️ You step into the buzzing Town — tall buildings, traffic and energy all around.")
    separator()

    print(''' ⇄ 🔒 You Have Four Places To Visit:

>>  1. City Mall             --> Press 1
>>  2. Car Showroom          --> Press 2
>>  3. Gun Inventory Store   --> Press 3
>>  4. Beach                 --> Press 4
>>  5. Random                --> Press 5
    ''')

    try:
        choice = int(input(">> Enter Your Choice: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return

    if choice == 1:
        separator()
        print("Entering City Mall... 🛍️")
        time.sleep(2)
        CityMall()

    elif choice == 2:
        separator()
        print("Visiting Car Showroom... 🚗")
        time.sleep(2)
        CarShowroom()

    elif choice == 3:
        separator()
        print("Sneaking into Gun Inventory Store... 🔫")
        time.sleep(2)
        GunInventory()

    elif choice == 4:
        separator()
        print("Heading to the Beach... 🏖️")
        time.sleep(2)
        Beach()

    elif choice == 5:
        step = random.choice([1, 2, 3, 4])
        separator()
        print("Teleporting to a random location in Town...")
        time.sleep(2)
        if step == 1:
            CityMall()
        elif step == 2:
            CarShowroom()
        elif step == 3:
            GunInventory()
        elif step == 4:
            Beach()
    else:
        print("❌ Invalid choice!")


# Forest

def Forest():
    time.sleep(2)
    print("🌲 You step into the dark and mysterious Forest. Birds chirping, wind rustling...")
    separator()

    print(''' ⇄ 🌿 You Have Four Places To Visit:

>>  1. Explore the Cave         --> Press 1
>>  2. Inspect the Old Tree     --> Press 2
>>  3. Enter Hunting Zone       --> Press 3
>>  4. Visit Herbal Hut         --> Press 4
>>  5. Explore Waterfall        --> Press 5
>>  6. Random                   --> Press 6

    ''')

    try:
        choice = int(input(">> Enter Your Choice: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return

    if choice == 1:
        separator()
        print("Entering the Cave... 🕳️")
        time.sleep(2)
        ForestCave()

    elif choice == 2:
        separator()
        print("Walking toward the Old Tree... 🌳")
        time.sleep(2)
        OldTree()

    elif choice == 3:
        separator()
        print("Stepping into the Hunting Zone... 🦌")
        time.sleep(2)
        HuntingZone()

    elif choice == 4:
        separator()
        print("Visiting the Herbal Hut... 🍃")
        time.sleep(2)
        HerbalHut()

    elif choice == 5:
        separator()
        print("Walking towards the roaring Waterfall... 🌊")
        time.sleep(2)
        Waterfall()

    elif choice == 6:

        step = random.choice([1, 2, 3, 4,5])
        separator()
        print("Teleporting to a random location in the Forest...")
        time.sleep(2)
        if step == 1:
            ForestCave()
        elif step == 2:
            OldTree()
        elif step == 3:
            HuntingZone()
        elif step == 4:
            HerbalHut()
        elif step == 5:
            Waterfall()

    else:
        print("❌ Invalid choice!")


# Village Sub Cases

def LandLord():
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
    print("Landlord is opening the treasure box... 🗃️")
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



def Farm():
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


def Temple():
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



def Well():
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


def Market():
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


# Town Sub Cases

def CityMall():
    print("\nYou enter a luxurious mall full of shiny shops and food aroma.")
    time.sleep(2)

    try:
        choice = int(input('''\nWhat do you want to do?

>>  1. Do Shopping 🛒
>>  2. Try Street Food 🌮

Your Choice: '''))
    except ValueError:
        print("❌ Invalid input.")
        return

    separator()
    time.sleep(3)

    if choice == 1:
        outcome = random.choice(["good", "bad"])
        if outcome == "good":
            print("✅ Great deal! You bought premium clothes at discount.")
            print("You Win 🏆")
        else:
            print("😤 You got scammed with fake branded items.")
            print("You Lose 💀")
    elif choice == 2:
        outcome = random.choice(["tasty", "poison"])
        if outcome == "tasty":
            print("😋 The food was delicious and spicy. You loved it!")
            print("You Win 🍔")
        else:
            print("🤢 Oops! Food poisoning ruined your day.")
            print("You Lose 💀")
    else:
        print("❌ Invalid choice!")

def CarShowroom():
    print("\nYou enter a shiny car showroom with luxury vehicles around.")
    time.sleep(2)

    try:
        choice = int(input('''\nWhat do you want to do?

>>  1. Take a Test Drive 🚘
>>  2. Try to Bargain 🤝

Your Choice: '''))
    except ValueError:
        print("❌ Invalid input.")
        return

    separator()
    time.sleep(3)

    if choice == 1:
        outcome = random.choice(["smooth", "crash"])
        if outcome == "smooth":
            print("🚗 You had an amazing test drive! Felt like a dream.")
            print("You Win 🏆")
        else:
            print("💥 You crashed into a pole during the drive!")
            print("You Lose 💀")
    elif choice == 2:
        outcome = random.choice(["discount", "insult"])
        if outcome == "discount":
            print("🎉 You negotiated well and got a solid discount!")
            print("You Win 🏆")
        else:
            print("😡 Manager mocked you and kicked you out.")
            print("You Lose 💔")
    else:
        print("❌ Invalid choice!")

def GunInventory():
    print("\nYou enter a secured gun storage — crates, rifles, and security everywhere.")
    time.sleep(2)

    try:
        choice = int(input('''\nWhat do you want to do?

>>  1. Open a random crate 📦
>>  2. Talk to the guard 👮‍♂️

Your Choice: '''))
    except ValueError:
        print("❌ Invalid input.")
        return

    separator()
    time.sleep(3)

    if choice == 1:
        outcome = random.choice(["guns", "blast"])
        if outcome == "guns":
            print("🔫 Jackpot! The crate had rare guns and armor.")
            print("You Win 🏆")
        else:
            print("💣 Boom! The crate had explosives and it went off.")
            print("You Lose 💀")
    elif choice == 2:
        outcome = random.choice(["friendly", "arrest"])
        if outcome == "friendly":
            print("👮‍♂️ Guard trusted you and gave secret access.")
            print("You Win 🏆")
        else:
            print("🚔 Guard called cops and got you arrested!")
            print("You Lose 🚨")
    else:
        print("❌ Invalid choice!")

def Beach():
    print("\nYou arrive at a beautiful beach with golden sand and waves crashing.")
    time.sleep(2)

    try:
        choice = int(input('''\nWhat do you want to do?

>>  1. Swim in the Sea 🏊‍♂️
>>  2. Build a Sandcastle 🏰

Your Choice: '''))
    except ValueError:
        print("❌ Invalid input.")
        return

    separator()
    time.sleep(3)

    if choice == 1:
        outcome = random.choice(["refresh", "drown"])
        if outcome == "refresh":
            print("🌊 That swim was refreshing and peaceful.")
            print("You Win 🏆")
        else:
            print("😱 You got caught in a wave and drowned.")
            print("You Lose 💀")
    elif choice == 2:
        outcome = random.choice(["castle", "crabs"])
        if outcome == "castle":
            print("🏰 You made a stunning sandcastle. People applauded.")
            print("You Win 🏆")
        else:
            print("🦀 Crabs attacked your feet while digging!")
            print("You Lose 💀")
    else:
        print("❌ Invalid choice!")


# Forest Sub Case

def ForestCave():
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

def OldTree():
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

def HuntingZone():
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

def HerbalHut():
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

def Waterfall():
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


start()

