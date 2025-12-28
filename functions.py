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


# Enclosing scope - nested function can access the variable of the function where it is nested 
# inner func can access outer func's variables

# outer func can not access the variable which is declare inside inner func

# nonlocal keyword to modify the variable

def outer_func():
  msg = 'Hello msg'
  res='hello'
  def inner_func():
    nonlocal res # allow modification of variable
    print('Inside inner func' + msg)
    res="world"
  inner_func()
  print(res)

outer_func()

# Global scope variable 

# variable define outside func scope - can used any where in program
# global keyword to make locally scoped variable to make it global

# built-in scope refers to all built-in functions , modules, keywords available everywhere