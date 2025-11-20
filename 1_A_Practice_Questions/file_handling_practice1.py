# f=open("1_A_Practice_Questions/practice.txt","w")
# f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java")

# f.close()

# #  Step 3 replace the all occurence Java with Python and read the data.

# with open("1_A_Practice_Questions/practice.txt","r") as f:
#     data=f.read()
#     new_data=data.replace("Java","Python")
#     print(new_data)
# with open("1_A_Practice_Questions/practice.txt","w") as f:
#    f.write(new_data)
# with open("1_A_Practice_Questions/practice.txt","r") as f:
#     data=f.read()

# # Step 2 found the word "learning".

#     if(data.find("learning")!=-1):
#         print("found")
#     else:
#         print("Not found")

# #  Step 3 display the lino_no in which the word "learning" is presentented.

# def line():
#     word="learning"
#     data=True
#     line_no=1
#     with open("1_A_Practice_Questions/practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no+=1
#     return -1

# print(line())

# # print the count of even numbers in file saperated by comma.

# with open("1_A_Practice_Questions/practice.txt","r") as f:
#     data=f.read()
#     print(data)
#     count=0
#     nums=data.split(",")
#     for val in nums:
#         if(int(val)%2==0):
#             count +=1
# print( "Total even no.",count)