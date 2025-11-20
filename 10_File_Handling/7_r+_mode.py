f=open("10_File_Handling/sample.txt","r+") # r+ mode is use to over write the data to starting at the privious data and it is use to read and write a file.
f.write("abc")
print(f.read()) # the output is m a programmer because the pointer is move on m.
f.close()