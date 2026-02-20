def sum_of_natural_number(n):
  return n * (n+1) // 2


def sum_natural_number_recur(n):
  if n == 1:
    return 1
  return n + sum_natural_number_recur(n-1)

def loop_sum_natural_number(n):
  sum = 0
  i = 1
  for i in range(i, n+1):
    sum += i
  return sum

if __name__ == "__main__":
  n = 5
  print(sum_of_natural_number(n))
  m = 6
  print(sum_natural_number_recur(m))
  c = 4
  print(loop_sum_natural_number(c))