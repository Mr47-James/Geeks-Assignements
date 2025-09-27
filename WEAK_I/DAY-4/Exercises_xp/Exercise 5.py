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


# ----------- Example Usage -----------

members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False,
     'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False,
     'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

# Create TheIncredibles instance
incredible_family = TheIncredibles("Incredibles", members)

# First presentation
incredible_family.incredible_presentation()

# Use powers
incredible_family.use_power("Michael")
incredible_family.use_power("Sarah")

# Add Baby Jack
incredible_family.born(
    name="Jack", age=1, gender="Male", is_child=True,
    power="Unknown Power", incredible_name="BabyJack"
)

# Second presentation (after adding Jack)
incredible_family.incredible_presentation()

# Attempt to use power of Baby Jack (should raise exception)
try:
    incredible_family.use_power("Jack")
except Exception as e:
    print("Error:", e)
