#Program to demonstrate tuple operations (accessing, updating, deleting elements).  
# Creating a tuple
my_tuple = ("apple", "banana", "cherry", "date")
print("Original Tuple:", my_tuple)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Updating elements (convert to list first)
temp_list = list(my_tuple)
temp_list[1] = "blueberry"  # changing 'banana' to 'blueberry'
updated_tuple = tuple(temp_list)
print("Updated Tuple:", updated_tuple)

# Deleting an element (convert to list first)
temp_list = list(updated_tuple)
del temp_list[2]  # removing 'cherry'
final_tuple = tuple(temp_list)
print("Tuple after deletion:", final_tuple)
