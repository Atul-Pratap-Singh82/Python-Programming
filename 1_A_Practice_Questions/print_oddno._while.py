# print only odd no. by given range.
n=int(input("Enter a range= "))
i=1
while i<=n:
    if i%2==0:
        i+=1
        continue
    print(i)
    i+=1