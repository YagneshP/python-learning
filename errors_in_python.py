import pdb

# pdb is a debugger for python
def divide(a, b):
  pdb.set_trace() # this will stop the execution of the program and open the pdb debugger
  return a / b

print(divide(10, 2))