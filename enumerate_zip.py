### enumerate() 
# - built in method to add counter(default 0) to an iterable and return enumerate object

# syntax => enumerate(iterable, start=0)
# iterable argument is required , else give TypeError

# mostly used in 'for' loop

### without enumerate , if you want to track index of an list

fruits = ['Apple', 'Banana', 'Orange', "Mango"]

index = 0

for fruit in fruits:
  message = f"{fruit} at {index} index"
  print(message)
  index += 1


### with enumerate

for index, fruit in enumerate(fruits) : # notice here we are unpacking value of tuple from the enumerate object , we can use for ... in for object in python , will learn more and add note for this 
  message = f"At {index}, there is {fruit}"
  print(message)


## you can pass start argument (from where count will start)
print("Let's start with 2 now")
for count, fruit in enumerate(fruits, 2):
  message = f"fruit is at count {count}"
  print(message)