### Loops are used to repeat code block for set of number of times

### ==== for loop ====

# - go through each element of the iterable object



programming_languages = ["Java", "Rust", "Go", "Python"]

# for ... in ... :
#   code block to repeat # -- should be indented otherwise will get IndentationError

for lang in programming_languages:
  print(lang)

# you can use it for string as well
# you can nest them

for char in 'code':
  print(char)


fruits = ["Mango", 'orange', 'Apple', 'Banana']
category = ['Fruit', 'Vegetable']

for cate in category:
  for fruit in fruits:
    print(cate, fruit)


#### while loop - it repeat the code block until condition is False

# while ...condition..:
#   code block


# Guess the number

secret_number = 7
guessed_number = 0

while secret_number != guessed_number:
  guessed_number = int(input("Guess the number between 1 to 9: "))
  if(guessed_number != secret_number) :
    print("ohh! you have missed, Try Again")
  
print(' Saat crore')
