#Program to demonstrate the scope of variables inside and outside a function.  
x = 300

def myfunc():
  x = 200
  print("Inside a function(local)",x)

myfunc()

print("Outside a function(global)",x)