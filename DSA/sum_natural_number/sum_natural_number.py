def sum_of_natural_number(n):
  return n * (n+1) // 2


def sum_natural_number_recur(n):
  if n == 1:
    return 1
  return n + sum_natural_number_recur(n-1)

if __name__ == "__main__":
  n = 5
  print(sum_of_natural_number(n))
  m = 6
  print(sum_natural_number_recur(m))