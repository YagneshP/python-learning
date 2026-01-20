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
  