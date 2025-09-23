# No, you cannot add items to a tuple directly because tuples are immutable in Python, but we still can create another tuple that countains the new value an then add them to the old one. 

my_tuple = (1, 2, 3)
my_tuple = my_tuple + (4, 5)
print(my_tuple)
