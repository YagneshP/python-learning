# using 'def' keyword with name of function with pair of parentheses  and a colon(:)
# if not provided function return 'None'

def sum_string():
  print("The total sum")

def total_sum(a, b):
  return a + b

sum_string()
sum = total_sum(4, 5)

print(sum)

# if required argument not passed it gives TypeError


## Scope in function

# LEGB rule

# L - Local scope - variables define in function and class can access within that function and class

def local_function_scope():
  my_var = 10
  print(my_var)

# print(my_var) access my_var outside the function gives NameError  