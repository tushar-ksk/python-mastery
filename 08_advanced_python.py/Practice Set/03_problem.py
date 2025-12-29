table = [str(7*i) for i in range(1, 11)]

print("\n".join(table))

print(str(table).replace("[", "").replace("]", "").replace(", ", "\n").replace("'", ""))  # last one replace is used because when we use str() in table it will add ' in the string