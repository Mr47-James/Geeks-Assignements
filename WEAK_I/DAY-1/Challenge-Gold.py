def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

age = int(input("Enter your age: "))
birth_year = int(input("Enter your birth year: "))


candles = age % 10
if candles == 0:
    candles = 10  

candle_str = "i" * candles
cake_top = f"       ___{candle_str}___"

cake = f"""{cake_top}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""

if is_leap_year(birth_year):
    print("🎉 Leap year baby! Two cakes for you!\n")
    print(cake)
    print(cake)
else:
    print(cake)
