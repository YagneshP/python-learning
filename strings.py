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