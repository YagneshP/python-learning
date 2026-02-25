def printNumber(n):
  if n <= 0: #base case (it handle the negative number also)
    return
  print(n)
  printNumber(n-1) # recursive case

printNumber(5)
  