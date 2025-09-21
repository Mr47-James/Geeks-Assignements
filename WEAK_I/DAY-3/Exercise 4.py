class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to {self.name}.")
        else:
            print(f"{new_animal} is already in the zoo!")

    def get_animals(self):
        
        if self.animals:
            print(f"Animals in {self.name}: {', '.join(self.animals)}")
        else:
            print(f"No animals in {self.name} yet.")

    def sell_animal(self, animal_sold):
        
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold from {self.name}.")
        else:
            print(f"{animal_sold} is not in the zoo!")

    def sort_animals(self):
        
        self.grouped_animals = {}
        for animal in sorted(self.animals):
            first_letter = animal[0].upper()
            if first_letter not in self.grouped_animals:
                self.grouped_animals[first_letter] = []
            self.grouped_animals[first_letter].append(animal)
        print("Animals have been sorted and grouped.")

    def get_groups(self):
        
        if hasattr(self, 'grouped_animals'):
            for letter, animals in self.grouped_animals.items():
                print(f"{letter}: {animals}")
        else:
            print("You need to sort the animals first using sort_animals().")



new_york_zoo = Zoo("New York Zoo")

new_york_zoo.add_animal("Giraffe")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Eel")
new_york_zoo.add_animal("Emu")
new_york_zoo.add_animal("Ape")


new_york_zoo.get_animals()


new_york_zoo.sell_animal("Bear")


new_york_zoo.get_animals()


new_york_zoo.sort_animals()


new_york_zoo.get_groups()
