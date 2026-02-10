def count_digit(n):
  if n == 0:
    return 1
  
  count = 0

  while n != 0:
    #removing right most digit 
     n = n // 10

     count += 1

  return count

if __name__ == "__main__":
    n = 58964
    print(count_digit(n))