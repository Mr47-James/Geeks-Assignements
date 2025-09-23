import random
i = int(input(f"\nPut in a random number in range of 1-100: "))
def f1():
    x = random.randint(i, 100)
    if i != x:
        print(f"\n[!] Better luck next time.\n{i}-{x}")  
    else:
        print(f"\m[*] Congratulations, you won the lottery !!!\n{i}-{x}")    
f1()
