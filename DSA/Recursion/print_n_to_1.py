def printNumber(n):
  if n == 0: #base case (it handle the negative number also)
    return
  print(n)
  # print(n, end=' ') 
  # print(n) — prints the number
  # end=' ' — specifies what to print at the end (replaces the default \n newline)
  printNumber(n-1) # recursive case

printNumber(5)
  