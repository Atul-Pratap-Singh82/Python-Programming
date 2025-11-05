#Program for Linear Search in a list of numbers.  
l=[1,5,6,8,4,7,9,2,3,11,12,15,14,17,18,19,15,20,23]
x=int(input("Enter a no. "))
found=False
for i in l:
    if(l[i]==x):
        print("Elements",x,"is found at",i)
        found=True
        break
if not found:
    print("Element",x,"is not found")