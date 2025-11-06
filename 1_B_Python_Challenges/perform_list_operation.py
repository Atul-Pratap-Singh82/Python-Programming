# Program to perform list operations: append, update, remove elements.  
list=["Atul","Ankit","Hemant","Sachin"]
print("Original list: ",list)
print("Step-1 Append operation")
list.append("Deepak")
list.append("Rinku")
print("After append: ",list)
print("Step-2 Update")
list[1]="Ansh"
print("After 1st update: ",list)
list[1:2]="Vansh","Kansh"
print("After 2nd update: ",list)
print("Step-3 Remove elements")
list.remove("Kansh")
print("After removing: ",list)
