'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([-1,0,1])
print("Enter\nS for Snake\nW for water\nG for gun")
youstr = input("Enter your choice: ").upper()
youdict = {
    "S":1,
    "W":-1,
    "G":0
        }
reversedict = {
    1 : "Snake",
    -1 : "Water",
    0 : "gun"
}
if youstr in youdict:

    you = youdict[youstr]

    print(f"You Chose {reversedict[you]}\nComputer Chose {reversedict[computer]}")
    if computer == you:
        print("Match Draw")
    else:
        if computer == -1 and you == 1:
            print ("You win")
        elif computer == -1 and you == 0:
            print ("You lose")
        elif computer == 1 and you == -1:
            print ("You lose")
        elif computer == 1 and you == 0:
            print ("You win")
        elif computer == 0 and you == -1:
            print ("You win")
        elif computer == 0 and you == 1:
            print ("You lose")
        else:
            print("Something went wrong!")

else:
    print("Invalid Input.\nPlease enter from S, W, G")