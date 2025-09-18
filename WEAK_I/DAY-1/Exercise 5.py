my_fav_numbers = {"0", "1", "3", "4"}
my_fav_numbers.add("7")
my_fav_numbers.add("9")
my_fav_numbers.discard("9")
friend_fav_numbers = {"5", "6", "8"}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)