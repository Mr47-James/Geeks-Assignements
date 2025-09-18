names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

LALA = input("Put your name: ")

if LALA in names:
    print(f"{LALA} index is {names.index(LALA)}")
else:
    print(f"{LALA} is not included in yourlist")