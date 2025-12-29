print("\nThis the program to find your word in your file....\n")

a = input(("Enter Your File Name >>> "))

try:
   with open(f"{a}.txt", "r") as f:
      list = f.readlines()

   b = input("Enter the word that you want to find >>> ").lower()
   
   found = False
   lineno=1
   for str in list:
      if b in str.lower():
         print(f'\n{b} found in line: {lineno}')
         found = True
      lineno+=1
      
   if not found:
         print(f"{b} not found")
   print("")
except:
   print(f"File name \'{a}\' not found in directory")
   print("")
      