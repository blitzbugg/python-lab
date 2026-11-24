#  create a list and perform the following methods - insert(),remove(),append(),len(),pop(),and clear() dynamically.
my_list = []

my_list.append(1)
my_list.append(2)
my_list.append(3)
print("After appending elements:", my_list)

my_list.insert(1, 10)
print("After inserting element at index 1:", my_list)

my_list.remove(2)
print("After removing element 2:", my_list)

print("Length of the list:", len(my_list))

popped_element = my_list.pop()
print("Popped element:", popped_element)
print("After popping element:", my_list)

my_list.clear()
print("After clearing the list:", my_list)