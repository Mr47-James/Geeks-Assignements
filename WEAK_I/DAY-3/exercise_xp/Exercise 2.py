class Dog:
    registery = {}
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

        Dog.registery[self.name] = self

    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)
print(f"Dog_Name :: {Dog.registery['Rex'].name}")
print(f"Dog_Height :: {Dog.registery['Rex'].height}")
davids_dog.bark()
davids_dog.jump()
print(f"Dog_Name :: {Dog.registery['Teacup'].name}")
print(f"Dog_Height :: {Dog.registery['Teacup'].height}")
sarahs_dog.bark()
sarahs_dog.jump()       

biggest_dog = None
max_height = 0

for dog in Dog.registery.values():
    if dog.height > max_height:
        max_height = dog.height
        biggest_dog = dog

if biggest_dog is not None:
    print(f"{biggest_dog.name} is the biggest: {biggest_dog.height} cm")
