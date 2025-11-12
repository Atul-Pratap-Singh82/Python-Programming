f=open("10_File_Handling/demo.txt")
data=f.read()#Read spacific latters for given no. of latters
print(data) 
line1=f.readline() #One by one read line
print(line1)

print(type(data))
f.close()