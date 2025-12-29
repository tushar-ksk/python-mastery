from random import randint

print('''
        >>Game<<
>>>> GUESS THE NUMBER <<<<
              

''')

aim = randint(1,100)


guesses = 1

while (aim != 0):
    
    guess = int(input("Guess a number from the set of first 100 natural numbers(from 1 to 100) >>> "))
    if guess == aim:
        print(f"You guessed the number {aim} correctly in {guesses} attempts.")
        break

    elif guess > aim :
        if (guess - aim) < 5:
            print("You are almost there\nguess slightly lower")
            guesses +=1
        elif (aim - guess) > 50:
            print("You are touching the sky\nTry to guess lower numeber")
            guesses +=1
        elif guess > 100:
            print("You crossed the range of input.")
        else:
            print("lower number please")
            guesses +=1

    elif guess < aim :

        if (aim - guess) < 5:
            print("You are almost there\nTry slightly higher number ")
            guesses +=1
        
        elif (aim - guess) > 50:
            print("You lags behind\nTry to guess higher numeber")
            guesses +=1

        elif guess < 1:
            print("Think higher\nAtlease enter in range of input.")

        else:
            print("higher number please")
            guesses +=1

       
with open("guesse.txt","a") as f:
    f.write(f"{guesses}\n")
    
