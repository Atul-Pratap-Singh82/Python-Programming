# Wap to find a greater number among 3 number entered by the user.
a=input("Enter first no.[a]: ")
b=input("Enter second no.[b]: ")
c=input("Enter third no.[c]: ")

if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
elif c>a and c>b:
    print("C is greater")
else:
    print("A and B and C are equal")
