f=open("10_File_Handling/wsample.txt","a+") # this is use to add the data in the last position.if you read the data the output is empty becouse the pointer is move away and you can write the data also output is empty.but data is write at the and.
print(f.read())
f.write("atul")

f.close()
