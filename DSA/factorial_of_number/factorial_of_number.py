def factorial(n):
  ans = 1
  i = 2
  while(i <= n):
    ans *= i
    i += 1
  return ans

# This approach has O(n) Time and O(1) space


## recusrive approach
def factorial_recursive(n):
  if n == 0:
    return 1
  return n * factorial_recursive(n-1)


if __name__ == "__main__":
  n = 5
  m = 6
  print(factorial(n))
  print(factorial_recursive(m))

