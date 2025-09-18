import random
def throw_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_times = 0
    History = []
    doubles = 0
def throw_until_doubles():
    while dice1 != dice2:
        while doubles <= 100:
            throw_dice()
            dice_times += 1
            if dice1 == dice2:    
                doubles += 1
            History.append((dice1, dice2))
            print(f"\n[*]Rolls: {dice_times} ::: {dice1} :: {dice2} ::: {doubles}")
        return print(f"it took {dice_times} throws to reach a 100 doubles")
        print(f"the average number of throws is: {}")
    return History
        
    
#throw_until_doubles = lambda : 
throw_dice()
