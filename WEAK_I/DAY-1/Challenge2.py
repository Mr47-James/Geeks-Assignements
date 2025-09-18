text = input("Enter a string: ")

result = "" 
prev_char = ""  

for char in text:
    if char != prev_char:   
        result += char
    prev_char = char

print("Result:", result)
