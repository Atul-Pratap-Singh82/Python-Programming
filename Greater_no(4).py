# Wap to find a greater number among 4 number entered by the user.
a=int(input("Enter first no.[a]: "))
b=int(input("Enter second no.[b]: "))
c=int(input("Enter third no.[c]: "))
d=int(input("Enter fourth no.[d]: "))

if(a>b and a>c and a>d):
    print("A is greater")
elif(b>c and b>d):
    print("B is greater")
elif(c>d):
    print("C is greater")
else:
    print("D is greater")