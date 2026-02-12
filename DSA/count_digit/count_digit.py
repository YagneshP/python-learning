import math
# Iterative approach - O(log n)
def count_digit_1(n):
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
    print(count_digit_1(n))

  
## Recursive approach - O(log n)

def count_digit_2(n):
   # Base case: if 'n' is single digit
   if n // 10 == 0:
      return 1
   
   return 1 + count_digit_2(n//10)

if __name__ == "__main__":
    n = 58964
    print(count_digit_2(n))


# Using log base 10

def count_digit_3(n):
   return math.floor(math.log10(n) + 1)

if __name__ == '__main__':
   n = 58964
   print(count_digit_3(n))