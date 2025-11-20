f=open("10_File_Handling/demo.txt","r")
data=f.readline() # we can not use the readline after read method becouse if read the entire data than the pointer move out and output in readline is empaty
print(data)