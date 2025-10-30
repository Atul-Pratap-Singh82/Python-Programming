l=(1,4,9,16,25,36,49,64,81,100,4,9)
x=int(input("Enter a no.= "))
ind=0
for n in l:
    if n==x:
        print("The no.",x,"is found at index", ind)

    ind+=1
print("END")
