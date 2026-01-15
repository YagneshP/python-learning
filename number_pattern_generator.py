def number_pattern(n):
  if not isinstance(n, int):
    return "Argument must be an integer value."
  if n < 1:
    return "Argument must be an integer greater than 0."
  result = ''
  for i in range(1, n+1):
    result += str(i) + ' '
  
  return result.strip()

number_pattern(4)

# # explain the above code
# # we are using the for loop to iterate over the range of 1 to n+1
# # we are using the str function to convert the integer to a string
# # we are using the += operator to add the string to the result
# # we are returning the result