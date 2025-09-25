# Exercise 1
birthdays = {
    "lara": "1989/12/14",
    "melissa": "1898/05/03",
    "james": "1455/11/16",
    "karlin": "1555/03/19",
    "ronald": "1333/08/14"
}

X = input("[!] Put your name here please: ")
print(f"W3lcome Mr.{X}")

LUKA = input("[+] You can look up the birthdays of the people in the list!\n").lower()

print(f"The birthday of Mr(s).{LUKA.capitalize()} is {birthdays.get(LUKA)}")
# Exercise 2
birthdays = {
    "lara": "1989/12/14",
    "melissa": "1898/05/03",
    "james": "1455/11/16",
    "karlin": "1555/03/19",
    "ronald": "1333/08/14"
}

X = input("[!] Put your name here please: ")
print(f"W3lcome Mr.{X}")


print("\nAvailable names:", ", ".join(name.capitalize() for name in birthdays.keys()))

LUKA = input("[+] You can look up the birthdays of the people in the list!\n").strip().lower()

if LUKA in birthdays:
    print(f"The birthday of Mr(s).{LUKA.capitalize()} is {birthdays[LUKA]}")
else:
    print(f"Sorry, we don’t have the birthday information for {LUKA.capitalize()}.")

# Exercise 3
X = str(input("Put in your Integer: "))
def parma(X):
    calc = int(X) + int(X * 2) + int(X * 3) + int(X * 4)
    print(f"\nYour Output is {calc}")
parma(X)

# Exercise 4
import random

def throw_dice():
    """Simulate throwing two dice and return their values as a tuple."""
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

def throw_until_doubles(max_doubles=100):
    throws = 0
    doubles = 0
    combinations = []  
    throws_to_doubles = []  
    while doubles < max_doubles:
        dice1, dice2 = throw_dice()
        throws += 1
        combinations.append((dice1, dice2))

        if dice1 == dice2:  
            doubles += 1
            throws_to_doubles.append(throws) 
            print(f"Double #{doubles} caught: {dice1}, {dice2} after {throws} throws")

    average = sum(throws_to_doubles) / len(throws_to_doubles)

    print(f"\nTotal throws: {throws}")
    print(f"\nAverage throws to reach doubles: {average:.2f}")

throw_until_doubles()

  
