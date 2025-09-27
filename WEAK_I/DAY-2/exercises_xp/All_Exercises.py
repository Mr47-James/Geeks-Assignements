# Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

x = dict(zip(keys, values))

print(x)

# Exercise 2
family = {}
Total_fee = 0

while True:
    x = input("Put in your name (or 'q' to Quit): ")
    if x.lower() == "q":
        print(f"\nTotal price is: {Total_fee}$")
        break
    
    a = input("Put in your age (or 'q' to Quit): ")
    if a.lower() == "q":
        print(f"\nTotal price is: {Total_fee}$")
        break
    else:
        a = int(a)  # only convert if not quitting

    family[x] = a  

    # Ticket calculation only for this new person
    if a <= 3:
        price = 0
        print("\nFree Access")
    elif 3 < a <= 12:
        price = 10
        print(f"\nYou have to pay: {price}$")
    else:
        price = 15
        print(f"\nYou are over 12, you should pay: {price}$")

    Total_fee += price

# Exercise 3
 brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2

print(f"Zara's clients are: {', '.join(brand['type_of_clothes'])}.")

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]

print("Last competitor:", brand["international_competitors"][-1])

print("US major colors:", brand["major_color"]["US"])


print("Number of key-value pairs:", len(brand))

print("Keys:", brand.keys())

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)

print("Updated number of stores:", brand["number_stores"])

# Exercise 4
def describe_city(city, country="Tailand"):
    print(f"{city} is in {country}")
describe_city("Casablanca", "morocco")

# Exercise 5
import random
i = int(input(f"\nPut in a random number in range of 1-100: "))
def f1():
    x = random.randint(i, 100)
    if i != x:
        print(f"\n[!] Better luck next time.\n{i}-{x}")  
    else:
        print(f"\m[*] Congratulations, you won the lottery !!!\n{i}-{x}")    
f1()
# Exercise 6
def make_shirt(size="L", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{text}'.")

make_shirt()

make_shirt("M")

make_shirt("S", "Hello World!")

make_shirt(size="XL", text="Code > Sleep")

# Exercise 7
import random

def get_random_temp(season=None):
    """Return a random temperature depending on season"""
    if season == "winter":
        return random.uniform(-10, 16)   
    elif season == "spring":
        return random.uniform(16, 23)    
    elif season == "summer":
        return random.uniform(24, 40)    
    elif season == "autumn" or season == "fall":
        return random.uniform(16, 23)    
    else:
        # Default: full range
        return random.uniform(-10, 40)


def month_to_season(month: int):
    """Map month number to season"""
    if month in (12, 1, 2):
        return "winter"
    elif month in (3, 4, 5):
        return "spring"
    elif month in (6, 7, 8):
        return "summer"
    elif month in (9, 10, 11):
        return "autumn"


def main():
    
    choice = input("Do you want to enter a season or month? (s/m): ").strip().lower()
    
    if choice == "m":
        month = int(input("Enter month number (1–12): "))
        season = month_to_season(month)
    else:
        season = input("Enter a season (winter, spring, summer, autumn): ").strip().lower()

    temp = get_random_temp(season)
    print(f"\nThe temperature right now is {temp:.1f}°C")

    
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don’t forget your coat")
    elif 16 < temp <= 23:
        print("Nice weather! Maybe bring a light jacket")
    elif 24 <= temp <= 32:
        print("Warm day! Keep hydrated and wear light clothes")
    elif 32 < temp <= 40:
        print("That’s insane, send me a postcard from heaven")
    else:
        print("Unusual temperature range detected!")



main()

# Exercise 8 

import random

def get_random_temp(season=None):
    """Return a random temperature depending on season"""
    if season == "winter":
        return random.uniform(-10, 16)   
    elif season == "spring":
        return random.uniform(16, 23)    
    elif season == "summer":
        return random.uniform(24, 40)    
    elif season == "autumn" or season == "fall":
        return random.uniform(16, 23)    
    else:
        # Default: full range
        return random.uniform(-10, 40)


def month_to_season(month: int):
    """Map month number to season"""
    if month in (12, 1, 2):
        return "winter"
    elif month in (3, 4, 5):
        return "spring"
    elif month in (6, 7, 8):
        return "summer"
    elif month in (9, 10, 11):
        return "autumn"


def main():
    
    choice = input("Do you want to enter a season or month? (s/m): ").strip().lower()
    
    if choice == "m":
        month = int(input("Enter month number (1–12): "))
        season = month_to_season(month)
    else:
        season = input("Enter a season (winter, spring, summer, autumn): ").strip().lower()

    temp = get_random_temp(season)
    print(f"\nThe temperature right now is {temp:.1f}°C")

    
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don’t forget your coat")
    elif 16 < temp <= 23:
        print("Nice weather! Maybe bring a light jacket")
    elif 24 <= temp <= 32:
        print("Warm day! Keep hydrated and wear light clothes")
    elif 32 < temp <= 40:
        print("That’s insane, send me a postcard from heaven")
    else:
        print("Unusual temperature range detected!")



main()


    
