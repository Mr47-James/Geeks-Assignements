import random
class MyList:
    def __init__(self):
        self.mylist = []
        
    def rev(self, some_list):
        return list(reversed(some_list))

    def sorter(self, some_list):
        return sorted(some_list)

    def randomizer(self, some_list):
        self.mylist = []
        for _ in some_list:
            self.mylist.append(random.randint(1, 9))
        return self.mylist


ml = MyList()

List = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
        "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
        "U", "V", "W", "X", "Y", "Z"]

print(ml.rev(List))     
print(ml.sorter(List)) 
print(ml.randomizer(List))
