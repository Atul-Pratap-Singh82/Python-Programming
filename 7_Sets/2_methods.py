# add : this means that add a item in set like tuple ,str,int,float but not a list.
collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(5)
collection.add((1.0,9,9.5))
collection.add("atul")
print(collection)
# .remove : this means that remove a spacified element in sets.
collection.remove(1)
print(collection)
# .clear : this means that clear all elements of the sets and then return empty set.
# collection.clear()
# print(collection)
# pop : this means that pop random element of sets in every time pop different value.
print(collection.pop()) # pop 1
print(collection.pop()) # 2