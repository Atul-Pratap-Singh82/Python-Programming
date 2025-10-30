#Program to demonstrate string slicing and indexing.  
str="Atul Pratap Singh"
print("Indexing Operation")
print(str[0])
print(str[5])
print(str[9])
print("Slicing operation")
print(str[:]) # print all string items.
print(str[0:4])# print elements from 0-4 include "Atul".
print(str[4:12]) # print elements from 4-12 include " Pratap".
print(str[0:16:2]) # print elements from 0-16 but move second character after first elements.