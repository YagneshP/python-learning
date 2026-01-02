#### ============ Tuple =============== ###

# - same like list but tuple are "immutable" , can not change it

# - ordered sequence of values
# - can contain set of mixed data type

developer = ('Alice', 23, 'Python Developer')

# - TypeError if you update the tuple

#----- you will get TypeError if you try to update tuple by changing value of an element ------
# commented code below give the TypeError for assignment
# developer[0] = "Jane"


# - You can access by square bracket and index number
print("----- Accessing value from the tuple -------- ")
name = developer[0]
print("Getting first element value and assign to name : ",name)

# -- you can also use negative index for accessing element from back of the list
title = developer[-1]
print("Getting last element value  with negative index and assign to title : ", title)


# - if index number that exceeds or equal the length of tuple it gives IndexError

# --- tuple() constructor to create tuple ---
name = "Jessica"
name_tuple = tuple(name)
print(name_tuple)

# "in" keyword to check element in tuple or not , return True or False

print('o' in name_tuple)
print('J' in name_tuple)

# unpack value from tuple and assign to new variables

name, age, job = developer

print(name, age,  job)

# -- * asterisk for rest of the tuple value , which is in new tuple
# name, age = developer # ValueError: too many values to unpack (expected 2, got 3)
name, *rest = developer

print(rest)


## slicing tuple [start_index:stop_index:step]
# works same as list 

numbers = (1,2,3,4,5,6,7,8)
slice_nums = numbers[1::2] # using step
print(slice_nums)