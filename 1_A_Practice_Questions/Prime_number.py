n=int(input("Enter a range= "))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("this is not prime number")
            break
    else:
         print("Prime number")
else:
    print("Not a prime number")