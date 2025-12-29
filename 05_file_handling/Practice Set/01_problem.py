f = open("poem.txt")
a = f.read()
f.close

if "Twinkle" in a :
    print("The word \"Twinkle\" found in Poem")

else :
    print("The word \"Twinkle\" not found in Poem.")