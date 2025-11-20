with open("10_File_Handling/withkeyword.txt","r") as f:
    data=f.read()
    print(data)
    # in with keyword do not use the close method.because the with keyword is automatically close the file.
with open("10_File_Handling/withkeyword.txt","w") as f:
    f.write("abc") 

# with syntex is like a if statement that means you can have multiple with keyword and operation is perform on a given file saperatelly.
