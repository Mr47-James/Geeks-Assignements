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
