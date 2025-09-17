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

    
