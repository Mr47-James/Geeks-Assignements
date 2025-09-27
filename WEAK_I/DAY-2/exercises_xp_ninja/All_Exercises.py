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

# Exercise 3 XP NINJA

