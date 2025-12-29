# Snake Water Gun Game

import random

dict={"S": -1, "W": 1, "G": 0}

reversedict = {-1: "Snake", 1: "Water", 0:"Gun"}


def start():
    while True:

        computer = random.choice([-1,1,0])

        print('''
        >>Game<<
>>>> Snake Water Gun <<<<
              

''')
        print("Press S for Snake\nPress W for water\nPress G for gun\n")
        youstr = input("Enter Your Choice: ").upper()
        print("")
        print("")
        if youstr not in dict:
            print("Invalid input")
            break
                
        
        else:
            you = dict[youstr]
        
            print(f"Computer Chose {reversedict[computer]}\nYou Chose {reversedict[you]}\n")


            if you == computer:
                print("Match Draw!")

            else:

                    rules ={
                        #(Computer,You): result

                            (-1,0): 1, #You win 
                            (1,-1): 1, #You win 
                            (0,1):  1, #You win
                            (0,-1): 2, #You lose
                            (-1,1): 2, #You lose
                            (1,0) : 2  #You lose


                        }
                    result = rules.get((computer,you))

                    if result == 1:
                        print("you win")
                    else:
                        print("you lose")

            print('''
                
                    
                ''')

        z = input("press \"Enter\" if you want to play again.").upper()
        if z== "":
            print("Game started again ♥")
            continue
        
        else:
            
            print("You entered undefined key!\nGOOD BYE ♥")
            print("")
            print("")
            break
        

start()