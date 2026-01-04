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
