import pdb

# pdb is a debugger for python
def divide(a, b):
  # pdb.set_trace() # this will stop the execution of the program and open the pdb debugger
  # IDE debugger will also stop the execution of the program and open the debugger
  # Select the line of code you want to debug and click on the debugger icon
  # You can also set a breakpoint by clicking on the line of code and pressing F9
  return a / b

print(divide(10, 2))