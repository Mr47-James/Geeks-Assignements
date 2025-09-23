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
