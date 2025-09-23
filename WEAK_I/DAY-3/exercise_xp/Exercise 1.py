class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
    
        
c1 = Cat("Lili", 3)
c2 = Cat("Botler", 5)
c3 = Cat("Shiro", 2)
cats = [Cat("Lili", 3), Cat("Botler", 5), Cat("Shiro", 2)]
def younger(cats):
    return min(cats, key=lambda cat: cat.age)
youngest = younger(cats)
print(f"The youngest cat is {youngest.name} ::: {youngest.age}")
