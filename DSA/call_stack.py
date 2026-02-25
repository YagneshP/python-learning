# let understand call stack

def func2(n):
  print("func2 is added to callstack")
  print("we are in func2")
  print("n =", n)

def func3():
  print("func3 is added to callstack")
  print("we are in func3")


def func1(x):
  print('func1 added to call stack')
  print('calling func2')
  func2(x)
  print("func2 is removed from call stack")
  print("func1 is still in callstack")
  print('calling func3')
  func3()
  print("func3 is removed from call stack")
  print("this is the last statement from the func1 after that func1 will be removed from call stack")

# calling func1 , it will insert func1 in to call stack
func1("hi")