# Exercise 1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
Bengal_cat = Bengal("Leo", 3)
Chartreux_cat = Chartreux("Milo", 2)
Siamese_cat = Siamese("Luna", 1)

all_cats = [Bengal_cat, Chartreux_cat, Siamese_cat]

sara_pets = Pets(all_cats)
sara_pets.walk()

# Exercise 2
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):

        return (self.weight / self.age) * 10

    def fight(self, other_dog):

        self_strength = self.run_speed() * self.weight
        other_strength = other_dog.run_speed() * other_dog.weight

        if self_strength > other_strength:
            return f"{self.name} won the fight against {other_dog.name}!"
        elif self_strength < other_strength:
            return f"{other_dog.name} won the fight against {self.name}!"
        else:
            return f"The fight between {self.name} and {other_dog.name} is a draw!"



dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 15)
dog3 = Dog("Max", 7, 30)


print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(f"{dog1.name}'s speed: {dog1.run_speed()}")
print(f"{dog2.name}'s speed: {dog2.run_speed()}")
print(f"{dog3.name}'s speed: {dog3.run_speed()}")


print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog1.fight(dog3))

# Exercise 3
import random
from dog import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dog_names):
       
        all_dogs = ", ".join(dog_names)
        print(f"{self.name}, {all_dogs} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet and can't do tricks.")
# Exercise 4

class Family:
    def __init__(self, last_name, members=None):
        self.last_name = last_name
        self.members = members if members else []

    def born(self, **kwargs):
        """Add a new child to the family."""
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family on the birth of {kwargs['name']}!")

    def is_18(self, name):
        """Check if a family member is over 18."""
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        print(f"No member named {name} found in the {self.last_name} family.")
        return False

    def family_presentation(self):
        """Print the family last name and details of each member."""
        print(f"\nFamily {self.last_name} Presentation:")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, "
                  f"Gender: {member['gender']}, Is child: {member['is_child']}")


members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]


my_family = Family("Smith", members)


my_family.family_presentation()


my_family.born(name="Emma", age=0, gender="Female", is_child=True)


print("Is Michael over 18?", my_family.is_18("Michael"))
print("Is Emma over 18?", my_family.is_18("Emma"))


my_family.family_presentation()

# Exercise 5
class Family:
    def __init__(self, last_name, members=None):
        self.last_name = last_name
        self.members = members if members else []

    def born(self, **kwargs):
        """Add a new child to the family."""
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family on the birth of {kwargs['name']}!")

    def is_18(self, name):
        """Check if a family member is over 18."""
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        print(f"No member named {name} found in the {self.last_name} family.")
        return False

    def family_presentation(self):
        """Print the family last name and details of each member."""
        print(f"\nFamily {self.last_name} Presentation:")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, "
                  f"Gender: {member['gender']}, Is child: {member['is_child']}")


class TheIncredibles(Family):
    def __init__(self, last_name, members=None):
        super().__init__(last_name, members)

    def use_power(self, name):
        """Print a member's power if they are over 18, else raise an exception."""
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['name']}'s power is: {member['power']}")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old!")
                return
        print(f"No member named {name} found in the {self.last_name} family.")

    def incredible_presentation(self):
        """Print a presentation of the incredible family."""
        print("\n*** Here is our powerful family ***")
        super().family_presentation()
        for member in self.members:
            print(f"Incredible Name: {member['incredible_name']}, Power: {member['power']}")


members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False,
     'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False,
     'power': 'read minds', 'incredible_name': 'SuperWoman'}
]


incredible_family = TheIncredibles("Incredibles", members)


incredible_family.incredible_presentation()


incredible_family.use_power("Michael")
incredible_family.use_power("Sarah")


incredible_family.born(
    name="Jack", age=1, gender="Male", is_child=True,
    power="Unknown Power", incredible_name="BabyJack"
)


incredible_family.incredible_presentation()

try:
    incredible_family.use_power("Jack")
except Exception as e:
    print("Error:", e)
