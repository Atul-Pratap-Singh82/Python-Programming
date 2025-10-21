#Search for a number x in this tuple using loop.
# (1,4,9,16,25,36,49,64,81,100)
t=(1,4,9,16,25,36,49,64,81,100)
n=int(input("Enter a element= "))
i=0
while i<=len(t):
  if (t[i]==n):
      print("Found at index",i)
      break
  else:
      print("finding")
  i += 1

print("End of loop")