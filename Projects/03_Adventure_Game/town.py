from Startfunc import separator
import time
import random

def go_city_mall():
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

def go_car_showroom():
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

def go_gun_inventory():
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

def go_beach():
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

def go_random_in_town():
    step = random.choice([1, 2, 3, 4])
    print("Teleporting to a random location in Town...")
    time.sleep(2)
    if step == 1:
        print(" >> (Randomly) 🔓 You Entered City Mall")
        go_city_mall()
    elif step == 2:
        print(" >> (Randomly) 🔓 You Entered Car Showroom")
        go_car_showroom()
    elif step == 3:
        print(" >> (Randomly) 🔓 You Entered Gun Inventory Store")
        go_gun_inventory()
    elif step == 4:
        print(" >> (Randomly) 🔓 You Reached Near Beach")
        go_beach()

def go_town():
    print("Entering Town........")
    time.sleep(2)
    print("")
    print(" >> 🔓 You Entered Village")
    time.sleep(0.5)
    print("🏙️ You step into the buzzing Town — tall buildings, traffic and energy all around.")
    time.sleep(5)
    print("")
    print(''' ⇄ 🔒 You Have Four Places To Visit:

>>  1. City Mall           --> Press 1
>>  2. Car Showroom        --> Press 2
>>  3. Gun Inventory Store --> Press 3
>>  4. Beach               --> Press 4
>>  5. Random              --> Press 5
    ''')

    choices_town = {
        1: go_city_mall,
        2: go_car_showroom,
        3: go_gun_inventory,
        4: go_beach,
        5: go_random_in_town
    }

    try:
        choice = int(input(">> Enter Your Choice: "))
        if choice in choices_town:
            separator()
            choices_town[choice]()
        else:
            print("❌ Invalid choice!")
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")