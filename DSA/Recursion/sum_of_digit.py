def sum_of_digit(n):
  if n < 10: # the base case is  when there is single digit just return it
    return n
  last_digit = n % 10
  return last_digit + sum_of_digit(n // 10)

print(sum_of_digit(984))
print(sum_of_digit(1))
