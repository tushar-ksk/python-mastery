import random                                             # built in module to generate random number

def game():                                               # definig a new function "game"
    print("")
    print("You are Playing a luck game.....")
    print("")
    a = input("Press enter to generate a number.")
    print("")
    if a == "":

        with open("game.txt") as f :                          # opening file for storing high score of game

            score = random.randint(0,101)                     # selecting random number from 1 to 100

            highscore = f.read()                              # reading highscore from file

            if not highscore:
                highscore = 0
            else:
                highscore = int(highscore)

        print(f"Your score is {score}")
        print("")
        with open("game.txt","w") as f:
            if highscore < score :
                f.write(str(score))
                print(f"You got a new highscore: {score}")
            
            else:
                f.write(str(highscore))
                print(f"But, your old highscore is {highscore}.\nBetter luck, try next time.\n")

    else:
        print("Thank you")       

game()