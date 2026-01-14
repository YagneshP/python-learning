### you can write list comprehension in a function

even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# for if else condition

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [(i, 'even') if i % 2 == 0 else (i, 'odd') for i in numbers]
print(even_numbers)

# explain the above code
# we are creating a list of tuples
# the first element of the tuple is the number
# the second element of the tuple is 'even' if the number is even, otherwise 'odd'
# we are using the if else condition to create the list of tuples
# we are using the for loop to iterate over the numbers
# we are using the if else condition to create the list of tuples

### filter function

def is_long_word(word):
    return len(word) > 5

words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
long_words = filter(is_long_word, words) # filter function returns a filter object
print(list(long_words)) # we are using the list function to convert the filter object to a list


# map function

def double_number(number):
    return number * 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doubled_numbers = map(double_number, numbers) # map function returns a map object
print(list(doubled_numbers)) # we are using the list function to convert the map object to a list

# explain the above code
# we are using the map function to double the numbers
# the map function takes a function and a list as arguments
# the function is the double_number function that returns the number multiplied by 2
# the list is the list of numbers
# the map function returns a new list with the numbers multiplied by 2
# we are using the list function to convert the map object to a list



## sum function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_numbers = sum(numbers) # sum function returns the sum of the numbers
print(sum_of_numbers)

# explain the above code
# we are using the sum function to sum the numbers
# the sum function takes a list as an argument
# the sum function returns the sum of the numbers
# we are using the print function to print the sum of the numbers

# sum function also takes a start value as an argument

sum_of_numbers = sum(numbers, 10) # sum function returns the sum of the numbers + 10
print(sum_of_numbers)

## lambda function

# use inline lambda function to double the numbers

doubled_numbers = map(lambda x: x * 2, numbers) # map function returns a map object
print(list(doubled_numbers)) # we are using the list function to convert the map object to a list

# explain the above code
# we are using the map function to double the numbers
# the map function takes a function and a list as arguments
# the function is a lambda function that returns the number multiplied by 2
# the list is the list of numbers
# the map function returns a new list with the numbers multiplied by 2
# we are using the list function to convert the map object to a list