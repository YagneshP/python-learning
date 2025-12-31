####### ---- List Data type ---- ######


# ordered sequence elements data type
# can store number, string , other lists
# Mutable
# zero-based index - first element at 0 index

skills = ['javascript', 'react', 'python', ['css', 'scss', 1]]

# to access the element from the list --> reference the index number in sequence

element_0 = skills[0]
print(element_0) # should print ---> 'javascript'

# Negative index used to access element from end of the list
# -1 to access last element from the list , and so on

last_element = skills[-1]
print(last_element) # should print last element which is a list ------> ['css', 'scss', 1]


# list() - constructor use to convert iterable into list
# iterable object can be looped one element at a time.
print(list(element_0)) # convert string in to list and should print ---> ['j', 'a', 'v', 'a', 's', 'c', 'r', 'i', 'p', 't']

# to get Total number of element use "len()"

print(len(list(element_0))) # should print 10 , here we convert first element which is string 'javascript' in to list and finding total number element of that list 

# List are mutable so you can update a value (element) at particular index
# if you any out of bound index(positive or negative) for particular list it gives 'IndexError'

skills[1] = 'nextJs' # here we are changing second element value from 'react' to 'nextJs'

print(skills) # should print ['javascript', 'nextJs', 'python', ['css', 'scss', 1]]