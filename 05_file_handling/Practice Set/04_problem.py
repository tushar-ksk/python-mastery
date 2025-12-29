
with open("file.txt","r") as f:
    a= f.read()
    c = a.replace("donkey" , "######").replace("Donkey" , "######")
    if "donkey" or "Doneky" in a:
        print("\nThe word DONKEY is found.\n")
        b=input("Press enter if you want to replace the word DONKEY with ###### ")
        print("")
        if b == "":
            with open("file.txt", "w")as f:
                f.write(c)
            print("The word Donkey replaced with ###### successfully..\n")

        else:
            print("You refused the suggestion...\n\nThank You...")
    else:
        print("\nThe word DONKEY is not found.\n")