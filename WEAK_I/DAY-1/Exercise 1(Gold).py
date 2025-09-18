Month = int(input("Enter your Mounth: "))

match Month:
    case 12 | 1 | 2:
        print("Winter")
    case 3 | 4 | 5:
        print("spring")
    case 6 | 7 | 8:
        print("Summer")
    case 9 | 10 | 11:
        print("Autumn")
    