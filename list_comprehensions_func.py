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


