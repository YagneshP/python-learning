#### range()

# - this function use for generating sequence of integers

start_point = 1
stop_point = 5  # stop argument is required for this function
step= 2


## ==== with stop only ====
range_with_stop_only = range(stop_point)

print(range_with_stop_only) # this will print range(0,5)
# if start argument not provided , range start from 0

for num in range_with_stop_only:
  print(num) # start with 0 and end at 4 , 
  ## notice 5 is not included because it is non-inclusive


## === with start and stop ===
range_with_start_stop = range(start_point, stop_point)
print(range_with_start_stop)

for num in range_with_start_stop:
  print(num) # here it start with 1 , because we provided start argument

## === with start,stop and step ====
range_with_step = range(start_point, 10, step) # using 10 as stop 
print(range_with_step)

for num in range_with_step:
  print(num) 


# range() - it requires at least 1 argument , if you don't pass any you will get TypeError
# range() # uncomment this and run you will get TypeError

# - it takes only integer as arguments , if you pass float/string it gives you TypeError
# range(3.4) # uncomment this and run you will get TypeError: 'float' object cannot be interpreted as an integer


### Decrement order range

decrement = range(5, 0, -1)
print(decrement)

for num in decrement:
  print(num) # notice here: 0 not include because that is stop argument and it start from 5 to 1