# Using Recursion and two pointer
#.  L  R
#.  |  |
#.  v  v
#  'abba'

# Initialize two pointers: one to point to starting index and one to point to ending index. Compare the characters at starting and ending indices. If the characters match, recursively check for inner substring. Otherwise, return false

def isPalindromRec(s, left, right):

  #Base Case

  if left >= right:
    return True
  
  #if mismatch found

  if s[left] != s[right]:
    return False
  
  return isPalindromRec(s, left+1, right-1)

def isPalindrome(s):
  return isPalindromRec(s, 0, len(s)-1)


if __name__ == "__main__":
    s = "abba"
    
    if isPalindrome(s):
        print("true")
    else:
        print("false")