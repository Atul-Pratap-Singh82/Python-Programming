#Program to create a basic calculator using if-else statements. 
a=int(input("Enter 1st no= "))
b=int(input("Enter 2nd no= "))
print("Choices for different operation")
print("1--> Addition")
print("2--> Subtraction")
print("3--> Multiplication")
print("4--> Division")
c=int(input("Enter a choice= "))
if(c==1):
    s=a+b
    print("Addition of",a,"and",b,"is: ",s)
elif(c==2):
    s=a-b
    print("Subtraction of",a,"and",b,"is: ",s)
elif(c==3):
    s=a*b
    print("Multiplication of",a,"and",b,"is: ",s)
elif(c==4):
    if(b!=0):
        s=a/b
        print("Division of",a,"and",b,"is: ",s)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid choices please enter valid choice")

