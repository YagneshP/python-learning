
# What is palindrome number
# 121 -> is palindrome because from start to end and end to start we read it same

# We can solve it by getting reverse number from the number

# for example : num = 1234  -> we reverse it to -> revNum = 4321 and compare  num == revNum -> then its palindrome if num != revNum -> not palindrome


# How we are going to reverse the number (num = 1234)

# first we take out the last digit by 

##.    n%10  -> this gives the last digit
# here, it is 4

# now, we need to remove the last digit from the num
# we do that by num = num//10 -> same like Math.floor in js

# 1234 // 10 -> 123

# now, lets take out the last digit from 123
# 123 % 10 = 3


# now, what? if we store revNum = 4 we can multiply the revNum to 10 and add the last digit 3

# => 4*10 + 3 now revNum = 43

# so for the first step we can take revNum = 0

# same process follow --> 123 // 10 -> 12
# last digit --> 12 % 10 => 2
# revNum = 43 * 10 + 2 => 432

# 12 // 10 -> 1
# last digit --> 1 % 10 => 1
# revNum = 432 * 10 + 1 => 4321

# 1 // 10 -> 0
# Base case now num = 0
# we return revNum which is 4321 

#compare with num 1234 != 4321 -> not palindrome

def numRev(num, revNum):
  if(num == 0):
    return revNum
  
  revNum = revNum*10 + num%10
  return numRev(num // 10, revNum)

def numIsPalindrome(n):
    reversNum = numRev(n, 0)
    if n == reversNum:
       return "true"
    else:
       return "false"

print(numIsPalindrome(123))
print(numIsPalindrome(12321))

