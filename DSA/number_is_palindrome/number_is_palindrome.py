# palindrome means number is same if you read from the front or back
# for ex. 123321 -> This is palindrome
# 1234231 -> this is not palindrome


# Aproach 1:
# Need to reverse given n (number)
# will get the last digit using % modulo operator
# remove the last digit from n (will store in different variable for comparasion with reverse number)

# continue till temp become 0


def num_is_palindrome(n):
  reverse = 0
  temp = abs(n)

  while temp > 0:
    reverse = (reverse * 10) + (temp%10)
    temp = temp // 10

  return reverse == abs(n)

if __name__ == "__main__":
  n = 12321

  print(num_is_palindrome(n))