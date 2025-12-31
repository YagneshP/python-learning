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

# to remove any element from the list you can use 'del' keyword and reference the index number from where you want to "delete the element"

developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer) # ['Jane Doe', 'Python Developer']


# "in" keyword to check of element inside the list , return True or False

react_skill = "react" in skills
next_js_skill = "nextJs" in skills

print('react skill', react_skill) # should print react skill False
print('nextJs skill', next_js_skill) # should print nextJs skill True

## how to access the element from nested list

nested_element = skills[-1][0]
print('nested element is: ',nested_element)

# Unpacking value from the list (like destructure)

name , title = developer
print(name, title)

# if you need to collect any remaining elements from the list , use (*) asterisk operator

top_language, *rest = skills # rest will be remaining items list
print('top language', top_language)
print('other skills', rest)