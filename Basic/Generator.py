from collections.abc import Callable

def run(func:callable[[int|str],None],n:int)->None:
  """
  :this function is a wraper for the func with the iterables
  :params: n->no of inputs
  :returns: None
  >>> run(main,4)
  """
  func(n)

def runable(n:int|str)->None:
  """
  This returns the string or interger
  """
  # print("this provides a wraper for the func")
  print(f"this return the value {n}")

run(runable,30)
run(runable,"start")
