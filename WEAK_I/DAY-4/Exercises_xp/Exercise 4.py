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


# ----------- Example Usage -----------

members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

# Create Family instance
my_family = Family("Smith", members)

# Show presentation
my_family.family_presentation()

# Add a new child
my_family.born(name="Emma", age=0, gender="Female", is_child=True)

# Check age
print("Is Michael over 18?", my_family.is_18("Michael"))
print("Is Emma over 18?", my_family.is_18("Emma"))

# Show presentation again
my_family.family_presentation()
