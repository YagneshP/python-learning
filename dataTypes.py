name = 'John Doe' # string variable with single quote

last_name_changed = "Parekh" # string variable with double quote

# integer variable
age = 20
day = 10
month = 12
year = 2025

# float variable
height = 5.9
weight = 70.5
temperature = 36.5

# boolean variable
is_student = True  # note that True where T is capital and False where F is capital not like javascript
is_employee = False

# complex variable
complex_number = 1j
complex_number = 1.0 + 2.0j # here you reassigned the value of complex_number variable
complex_number = 1.0 + 2.0j

# Set variable 
# Set is a collection of unique elements
set_variable = {1, 2, 3, 4, 5}
set_variable = {1, 2, 3, 4, 4, 4} # here you reassigned the value of set_variable variable, 4 is repeated so it will be ignored

print(set_variable)


# Dictionary variable
# Dictionary is a collection of key-value pairs
dictionary_variable = {1: 'one', 2: 'two', 3: 'three'}
dictionary_variable = {1: 'one', 2: 'two', 3: 'three', 4: 'four'} # here you reassigned the value of dictionary_variable variable, 4 is new key-value pair so it will be added

dictionary_variable[5] = 'five' # here you added a new key-value pair 5: 'five'
dictionary_variable['1'] = 'one_changed' 
dictionary_variable[1] = 'one_changed_again' # here you changed the value of key '1' from 'one' to 'one_changed_again'
print(dictionary_variable)

# characteristics of dictionary
# 1. unordered means that the key-value pairs are not in a specific order
# 2. mutable means that the key-value pairs can be changed
# 3. can contain duplicate keys
# 4. can be nested

# Tuple variable
# Tuple is a collection of ordered and immutable elements
tuple_variable = (1, 2, 3, 4, 5)
tuple_variable = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # here you reassigned the value of tuple_variable variable

tuple_variable = (2,1,6,5,2)

# tuple_variable[0] = 100 # here you tried to change the value of the first element from 1 to 100, but it will raise an error because tuple is immutable
print(tuple_variable)

# characteristics of tuple
# 1. ordered means that the elements are in a specific order
# 2. immutable means that the elements cannot be changed
# 3. can contain duplicate elements
# 4. can be nested
# 5. can be used as a key in a dictionary
# 6. can be used as a value in a dictionary
# 7. can be used as a key in a set
# 8. can be used as a value in a set
# 9. can be used as a key in a tuple
# 10. can be used as a value in a tuple
# 11. heterogeneous means that the elements can be of different types



# Range variable
# Range is a sequence of numbers
range_variable = range(10)
range_variable = range(10, 20)
range_variable = range(10, 20, 2)
print(range_variable)

# characteristics of range
# 1. ordered means that the numbers are in a specific order
# 2. immutable means that the numbers cannot be changed
# 3. can contain duplicate numbers
# 4. can be nested

# List variable
# List is a collection of ordered and mutable elements
list_variable = [1, 2, 3, 4, 5]
list_variable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # here you reassigned the value of list_variable variable
list_variable = [2,1,6,5,2]
list_variable = ["2", 1, {"name": "John", "age": 20}]
list_variable[0] = 100 # here you changed the value of the first element from "2" to 100
print(list_variable)

# characteristics of list
# 1. ordered means that the elements are in a specific order


# None variable
# None is a special value that represents no value
none_variable = None
print(none_variable)


greeting_message = "Hello, World!"

# greeting_message[0] = 'h' # here you tried to change the value of the first element from 'H' to 'h', but it will raise an error because string is immutable
print(greeting_message)



# type() function is used to get the type of a variable

my_var_1 = 'Hello world'
my_var_2 = 21
my_var_3 = 21.0
my_var_4 = True
my_var_5 = None
my_var_6 = [1, 2, 3, 4, 5]
my_var_7 = (1, 2, 3, 4, 5)
my_var_8 = {1: 'one', 2: 'two', 3: 'three'}
my_var_9 = {1, 2, 3, 4, 5}
my_var_10 = range(10)

print(type(my_var_1)) # <class 'str'>
print(type (my_var_2)) # <class 'int'>
print(type (my_var_3)) # <class 'float'>
print(type (my_var_4)) # <class 'bool'>
print(type (my_var_5)) # <class 'NoneType'>
print(type(my_var_6)) # <class 'list'>
print(type (my_var_8)) # <class 'dict'>
print(type (my_var_9)) # <class 'set'>
print(type (my_var_10)) # <class 'range'>

# isinstance() function is used to check if a variable is of a specific type , and return True or False (boolean)

print(isinstance(my_var_1, str)) # True
print(isinstance(my_var_1, int)) # False

# print(isinstance(true, bool)) # name error because true is not a variable, it is a keyword


# type hinting in python is a way to specify the type of a variable

def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2)) # 3
print(add(1, 2.0)) # type error because 2.0 is not an integer
print(add(1, "2")) # type error because "2" is not an integer
print(add(1, True)) # type error because True is not an integer
print(add(1, None)) # type error because None is not an integer
print(add(1, [1, 2, 3])) # type error because [1, 2, 3] is not an integer

# type hinting is not mandatory, it is just a way to specify the type of a variable
# it is used to help the developer to understand the code better

user_name: str = "John Doe"
user_age: int = 20

add(user_name, user_age) # won't give you squiggly lines in vscode but it will give you type error at runtime