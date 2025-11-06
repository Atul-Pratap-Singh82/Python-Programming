# Program to create and manipulate dictionaries (access, update, delete).  
detail={
    "name":"Atulprtapsingh",
    "roll":17,
    "class": "BCA",
    "stu":{
            "phone":8985234512
    }
}
print("Original list:",detail)
print("Accessing items")
print(detail["name"])
print(detail["class"])
print(detail["roll"])
print("Update")
detail["phone"]=9045720692
detail["name"]="Ankitsingh"
print("After update",detail)
print("Delete elements")
del detail["phone"]
print("After deleting an item:",detail)
detail.pop("roll")
print("After deleting:",detail)
detail.popitem()
print(detail)
new={"name":"atul","class":"BBA"}
detail.update(new)
print(detail)