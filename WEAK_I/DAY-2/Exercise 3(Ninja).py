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
