words = input("Put in a word: ").upper()
dicta = {}  # Initialize the dictionary before the loop

for index, char in enumerate(words):
    if char in dicta:
        dicta[char].append(index)
    else:
        dicta[char] = [index]

print(dicta)
