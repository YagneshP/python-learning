def printNumber(n):
  if n <= 0:
    return
  print(n)
  printNumber(n-1)

printNumber(5)
  