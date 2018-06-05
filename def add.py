def adding(el1,el2):
  a=el1+el2
  return "The addition of {} and {} is {}".format(el1,el2,a)
# can use return statement instead of print
# can use .format() method 
def add():
  print(adding(87576846,5764656))
  el1=int(input("Enter first number: "))
  el2=int(input("Enter second number: "))
  print(adding(el1,el2))
add()

