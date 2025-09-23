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
