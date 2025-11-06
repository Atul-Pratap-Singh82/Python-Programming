# Program to reverse a string and check if it is a palindrome.  
str=input("Enter a string: ")
print("Original string: ",str)
reverse_str=str[::-1]
print("After reverse: ",reverse_str)
print("Check palindrome or not")
if(str==reverse_str):
    print("String is palindrome")
else:
    print("String is not Palindrome")