birthdays = {
    "lara": "1989/12/14",
    "melissa": "1898/05/03",
    "james": "1455/11/16",
    "karlin": "1555/03/19",
    "ronald": "1333/08/14"
}

X = input("[!] Put your name here please: ")
print(f"W3lcome Mr.{X}")


print("\nAvailable names:", ", ".join(name.capitalize() for name in birthdays.keys()))

LUKA = input("[+] You can look up the birthdays of the people in the list!\n").strip().lower()

if LUKA in birthdays:
    print(f"The birthday of Mr(s).{LUKA.capitalize()} is {birthdays[LUKA]}")
else:
    print(f"Sorry, we don’t have the birthday information for {LUKA.capitalize()}.")
