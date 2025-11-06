#Program to genarate fibonacci series.
n=int(input("Enter a term: "))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a
    a=b
    b=c+b