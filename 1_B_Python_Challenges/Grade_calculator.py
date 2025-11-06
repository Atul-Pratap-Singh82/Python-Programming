#Program to create grade calculator based on student percentage.
n=float(input("Enter your marks/persantage: "))
if n>100:
    print("Invalid Input \n Please enter Valid input")
elif(n>=90 and n<=100):
    print("A+ Grade")
elif(n>=80 and n<90):
    print("A Grade")
elif(n>=70 and n<80):
    print("B+ Grade")
elif(n>=60 and n<70):
    print("B Grade")
elif(n>=50 and n<60):
    print("Average")
elif(n>=40 and n<50):
    print("Poor")
else:
    print("Fail \n Next Try Good Luck")