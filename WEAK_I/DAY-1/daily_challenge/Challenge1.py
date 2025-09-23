Number = int(input("Put a number here: "))
LN = int(input("Put your Length here: "))

coef = 1
LIST = [] 

for T in range(1, LN + 1):  
    Sol = Number * T
    LIST.append(Sol)
print(f"number: {Sol} >> {LIST}")


