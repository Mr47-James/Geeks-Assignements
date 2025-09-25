# Exercise 1
Month = int(input("Enter your Mounth: "))

match Month:
    case 12 | 1 | 2:
        print("Winter")
    case 3 | 4 | 5:
        print("spring")
    case 6 | 7 | 8:
        print("Summer")
    case 9 | 10 | 11:
        print("Autumn")
# Exercise 2
for i in range(21):

    print(i)
# Exercise 3
ONAME = "Original"
NAME = ""
while NAME != ONAME:
    NAME = input("yourname please: ")
# Exercise 4
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

LALA = input("Put your name: ")

if LALA in names:
    print(f"{LALA} index is {names.index(LALA)}")
else:
    print(f"{LALA} is not included in yourlist")

# Exercise 5
N1 = int(input("Input the 1st number:"))
N2 = int(input("Input the 2nd number:"))
N3 = int(input("Input the 3rd number: "))

print(f"The greatest number is: {max(N1, N2, N3)}")

# Exercise 6

import random

Wins = 0
Losses = 0

while True:
    I1 = input("Enter a number between 1 and 9 (or 'q' to quit): ")
    if I1 == "q":
        print(f"GoodBye ::: {Wins} Wins :: {Losses} Losses")
        break
    GN = random.randint(1, 9)
    if GN == I1:
        print('Winner')
        Wins += 1 
    else: 
        print("Better luck next time.")
        Losses += 1
