total=0
def sum(arg1,arg2):
  total=arg1+arg2
  print("Inside the function local total",total)
  return total
#sum(10,20)
#print("Outside the function global total",total)
def fn():
  a=' '
  str1=str(input("Enter 1st string: "))
  str2=str(input("Enter 2nd string: "))
  return "Concatenatedstring is:",str1+a+str2


def intfn():
  a=str(input("Enter a number: "))
  b=str(input("Enter 2nd number"))
  return  'Addition of integers in string format is', int(a)+int(b)
#print(intfn())
#print(fn())

def strln():
  str1=str(input("Enter 1st string: "))
  str2=str(input("Enter 2nd string: "))
  if len(str1)<len(str2):
    print(str1,"has the maximum length")
  elif len(str1)==len(str2):
    print("Both the strings have same length")
    print(str1)
    print(str2)
  else:
    print(str2,"has the maximum length")
#strln()


  
def poem():
  pm=("""Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;

Then took the other, as just as fair,
And having perhaps the better claim,
Because it was grassy and wanted wear;
Though as for that the passing there
Had worn them really about the same,

And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day!
Yet knowing how way leads on to way,
I doubted if I should ever come back.

I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and Iâ€”
I took the one less traveled by,
And that has made all the difference.""")
  print("The road not taken")
  print("{}\n -by Robert Frost.".format(pm))
  print(pm.count('I'))
  print(pm.replace('could not',"could'nt"))
#poem()

def dictsqrval():
  a=[]
  b=[]
  for i in range(1,4):
    a.append(i)
  print(a)
  for i in a:
    b.append(i**2)
  print(b)
  c=a+b
  d1=dict(c)
  print(c)
#dictsqrval()

def dict1():
  a={}
  for i in range(1,4):
    a[i]=i**2
  return a
#print(dict1())

def dict1():
  a={}
  for i in range(1,21):
    a[i]=i**2
  print(a)
  print(a.values())
#dict1()

def list1():
  a=[]
  for i in range(1,21):
    sqr=i**2
    a.append(sqr)
  print(a)
  print("First five values are: ",a[0:6])
  print("last five values are: ",a[-5:])
#list1()

def fact():
  for i in range(3):
    num=int(input("Enter a number"))
    if num%3==0 and (num%5==0):
      print("Fizz Buzz")
    elif num%5==0:
      print("Buzz")
    elif (num%3==0):
      print("Fizz")
fact()
