# Exercise 1 XP NINJA
X = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet, Toyota"
Brand = X.split(",")
Brand.sort(reverse=True)
#Counter = X.count("o")
crem = 0
icrem = 0
ical = len(Brand) - icrem 
nana = set(Brand)
for i in Brand:
    if i.find("o"):
        crem += 1
    if i.find("i"):
        icrem += 1
print(f'[*] Brand With No Duplicates: "{", ".join(set(Brand))}"')
print(f'[*] Brand Sorted: "{", ".join(sorted(set(Brand)))}"')
print(f'[*] Brand fully sorted: "{", ".join(b[::-1] for b in set(Brand))}"')


print(f"[*] Number of Letter <O>: {X.count('o')}")    
print(f"[*] Number of Manufacturer's Names with <o>: {crem}")
print(f"Number of Letter <i>: {X.count('i')}")    
print(f"Number of Manufacturer's Names without <i>: {ical}")
print(f"[*] Brands List: {Brand}")
print(f"[*] Total Number of Manufacturers:  {len(Brand)}")

# Exercise 2 XP NINJA
def get_full_name(first_name, last_name, middle_name=None):
    print(f"{first_name} {middle_name or ''} {last_name}")
get_full_name("John", "lee") # Way number 1
get_full_name(first_name="john", middle_name="hooker", last_name="lee") # Way number 2

# Exercise 3 XP NINJA

Morse_Dic = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/"   # Space between words
}

# Reverse dictionary
Reverse_Morse_Dic = {v: k for k, v in Morse_Dic.items()}

Imessage = input("Paste here your message: ").upper()
Mode = input("Select your Mode (Cipher=0, Decipher=1): ") or "0"

def Morse_Trans(Imessage, Mode):
    if Mode == "0":  # Cipher: Text → Morse
        translated = [Morse_Dic.get(char, "") for char in Imessage]
        print(f'[*] Morse Code:\n{" ".join(translated)}')

    elif Mode == "1":  # Decipher: Morse → Text
        words = Imessage.split(" / ")  # Split Morse words by "/"
        translated_words = []
        for word in words:
            letters = [Reverse_Morse_Dic.get(code, "") for code in word.split()]
            translated_words.append("".join(letters))
        print(f'[*] Deciphered Text:\n{" ".join(translated_words)}')

    else:
        print("[!] Invalid Mode. Please enter 0 for Cipher or 1 for Decipher.")

Morse_Trans(Imessage, Mode)

