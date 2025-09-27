class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        # Formula: (weight / age) * 10
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        # Strength is run_speed * weight
        self_strength = self.run_speed() * self.weight
        other_strength = other_dog.run_speed() * other_dog.weight

        if self_strength > other_strength:
            return f"{self.name} won the fight against {other_dog.name}!"
        elif self_strength < other_strength:
            return f"{other_dog.name} won the fight against {self.name}!"
        else:
            return f"The fight between {self.name} and {other_dog.name} is a draw!"


# Create 3 Dog instances
dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 15)
dog3 = Dog("Max", 7, 30)

# Test methods
print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(f"{dog1.name}'s speed: {dog1.run_speed()}")
print(f"{dog2.name}'s speed: {dog2.run_speed()}")
print(f"{dog3.name}'s speed: {dog3.run_speed()}")

# Simulate fights
print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog1.fight(dog3))
