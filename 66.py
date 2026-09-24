# Program to update a tuple using a list
my_tuple = (10, 20, 30, 40)

print("Original tuple:", my_tuple)

my_list = list(my_tuple)


my_list[1] = 25

print("Updated list:", my_list)


my_tuple = tuple(my_list)

print("Updated tuple:", my_tuple)

