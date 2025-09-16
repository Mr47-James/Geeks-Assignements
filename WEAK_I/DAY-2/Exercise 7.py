import random

def main():
    x = get_random_temp()
    print(f"the current room temperature in (c): {x}c")
    if x < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0<x<=16:
        print("Quite chilly! Don’t forget your coat")
    elif 16<x<=23:
        print("Today's temperature is balanced! wear some spring lite clothes")
    elif 24<x<=32:
        print("Ahhh, today is hot!keep hidrated, lite wearing")
    elif 32<x<=40:
        print("ahhh, thats insane, send me a post card from heaven")
def get_random_temp(season):
    gen = random.randint(-10, 40)
    match gen:
        case G if -10 < G <= 16:
            print("These is Winter")
        case G if 16 < G <= 23:
            print("These is Autumn")
        case G if 23 < G <= 32:
            print("These is Spring")
        case G if 32 < G <= 40:
            print("These is Summer")
            

