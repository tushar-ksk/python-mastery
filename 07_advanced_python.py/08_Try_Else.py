try:
    a = int(input("Enter a number: "))
    print("The number is:", a)

except Exception as e:
    print("An error occurred:", e)


else:
    print("I am in else block")

    # else will execute only if try block is executed successfully without any exception