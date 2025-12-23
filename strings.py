# with single quote
single_quote_string = 'Hello, World!'

# with double quote
double_quote_string = "Hello, World!"

# for multiline string use triple quotes """ or '''

multiline_string = """Hello, World!
This is a multiline string.
It can span multiple lines.
"""

multiline_string = '''Hello, World!
This is a multiline string.
It can span multiple lines.
'''

# if string contains single or double quote, use the other quote to define the string
single_quote_string = 'He said, "Hello, World!"'
double_quote_string = "He said, 'Hello, World!'"

# or we can use escape character \ to escape the quote
single_quote_string = 'He said. \"Hello, World!\"'

# string concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

# + only works with strings, not with other data types
name = "John"
age = 20

name_and_age = name + " " + age # this will raise a TypeError because age is not a string

# python doesn't support implicit type conversion, so we need to convert the data type to the same type
# we can use str() function to convert the data type to a string

name_and_age = name + " " + str(age) # this will work because we converted age to a string


# Augmented assignment operator for concatenation
# += perform concatenation and assignment

name = "John"
last_name = "Doe"

full_name = name
full_name += last_name
print(full_name)

# f-string means formatted strings

# f-string is a better way to concatenate strings also used for Interpolation
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)


# string interpolation
name = "John"
age = 20
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)



# string concatenation using f-string
full_name = f"{first_name} {last_name}"
print(full_name)

# string concatenation using format() method
full_name = "{} {}".format(first_name, last_name)
print(full_name)


# get a length of string and work with particular character from string , process called 'indexing'
my_str = "Hello world"
print(len(my_str))

# Each character has position called 'index' start with 0, you can access the character from string using '[]' square bracket

my_str = "Hello world"
print(my_str[0])
print(my_str[6])

# with negative indexing you can get character from end

print(my_str[-1]) # print last character from the string 'd'
print(my_str[-2]) # print second last character from the string 'l'

# if you -12 or 12 you will get the IndexError

# String slicing

# string[start:stop] - start index included , stop index not included

my_str = 'Hello World'
first_five_chars = my_str[0:6]
print(first_five_chars)
print(my_str[2:6])
print(my_str[0:4]) # start from 0 index 
print(my_str[:4]) # this also start from 0 index
print(my_str[:]) # This will output whole string
print(my_str[4:]) # This will start from index 4 till end of the string

#string[start:stop:step]

print(my_str[1:6:2]) # extract every second char from index 1


# A helpful trick you can do with the step parameter is to reverse a string by setting step to -1, and leaving start and stop blank:

my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH


# To check if character or set of characters exist in string use 'in'

my_str = "hello world"

print("h" in my_str) #  True
print("hello" in my_str) #True
print("f" in my_str) # False


# Different method for string

# upper() - new string with all characters with uppercase

my_str = "hello"

new_str = my_str.upper()

# lower() - return new string all lowercase characters

lowercase_str = new_str.lower()

# strip() - return new string with specified leading and trailing characters removed.
# if no argument passed it removes trailing and leading whitespace

my_str = '  hello world '
without_space_str = my_str.strip()

# replace(old, new) - return new string with all occurrence of `old` replaced by 'new'

my_str = 'hello world'

replaced_str = my_str.replace('hello', 'hi')


# split() - split string into list of string with specified 'separator' , if no separator provided will separate string with whitespace

my_str = 'Hello World'
split_str_list = my_str.split()
print(split_str_list)

# join element of list with join() and separator

my_str_list = ["hello", "world"]
joined_str = ' '.join(my_str_list) 


# startswith(prefix) - return boolean if string start with provided prefix

my_str = "hello world"

print(my_str.startswith('hello')) # True
