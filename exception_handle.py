try:
  x = (10 / 0)
except ZeroDivisionError:
  print("Error: Division by zero")
else:
  print("No error occurred")
finally:
  print("This will always execute")

# multiple exceptions

try:
  x = int('abc')
  result = 10 / x
except ValueError:
  print("Error: Invalid value")
except ZeroDivisionError:
  print("Error: Division by zero")
else:
  print("No error occurred")
finally:
  print("This will always execute")
  
# alias as 
try:
  x = int('abc')
  result = 10 / x
except ValueError as e:
  print(f"Error: {e}")
except ZeroDivisionError as e:
  print(f"Error: {e}")
else:
  print("No error occurred")
finally:
  print("This will always execute")

# multiple exceptions with a single except block
try:
  x = int(input("Enter a number: "))
  result = 10 / x
except (ValueError, ZeroDivisionError) as e:
  print(f"Error: {e}")
else:
  print("No error occurred")
finally:
  print("This will always execute")
  
# raise an exception with a custom message
def divide(a, b):
  if b == 0:
    raise ValueError("Division by zero is not allowed")
  return a / b

try:
  print(divide(10, 0))
except ValueError as e:
  print(f"Error: {e}") # this will print the custom message
