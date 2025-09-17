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
