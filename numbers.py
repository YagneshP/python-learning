# integers and floats - primary numeric data types

# integers - whole positive or negative numbers
from re import M


my_positive_int = 20
my_negative_int = -4

# Addition operation with '+' 

sum_of_ints = my_positive_int + my_negative_int
print(sum_of_ints) #16

# subtraction with '-' 

sub_of_ints = my_positive_int - my_negative_int
print(sub_of_ints)

# follows same math rules

# multiplication operation with '*'

multi_ints = my_positive_int * my_negative_int
print(multi_ints)

# division with '/'

divide_int = my_positive_int / my_negative_int # return float
print(divide_int)



# Floats - positive or negative number with decimal points

my_positive_floats = 1.1000400
my_negative_floats = -4.00043

# Addition with floats

add_floats = my_positive_floats + my_negative_floats

print(add_floats)

# subtraction of floats

sub_floats = my_positive_floats - my_negative_floats 
print(sub_floats)

# multiplication of floats 

multi_floats = my_positive_floats * my_negative_floats
print(multi_floats)

# division of floats 

divide_floats = my_positive_floats / my_negative_floats
print(divide_floats)

# if you mix int and float for operation python return float


# (%) modulo operator - return reminder when the value of left is divided by right value

my_int = 56
my_int_1 = 12

rem = my_int % my_int_1 # 56 / 12 => 12 * 4 = 48 , 56 - 48 = 8 (remainder)

# floor division with (//)

result_1 = 10 // 3 # => 3

# Explanation #
# The result of dividing 10 by 3 is 3.333...., but floor division returns the largest integer less than or equal to the result. Therefore, the result is 3.