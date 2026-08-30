d={"Name: ":"Arpita","age: ":12,"dob: ":2009}
d1={"Weight: ":45,'height: ':5.7}
# update()

print("update: ")
print("d: ",d)
print("d1: ",d1)
d.update({"age: ":20})

d.update({"gender: ":"Female"})
d1.update(d)
print(d)

print("         ")

# clear()
    # to clear the complete dictionary
    
d1.clear()
print("Clear: ",d1)
print("         ")
    
# pop(): remove key value pairs
print("D before pop: ",d)
d.pop('dob: ')
print("After pop: ",d)
print("         ")

# popitem(): remove last key-value from dict
print("Popitem(): ",d.popitem())

# del
# we can also use the del keyword to remove a dictionary item.
# If key is not provided, then the del keyword will delete the dictionary entirely.

d3={12:1,13:2,14:3,14:3,15:4}
del d3[12]
print("d3: ",d3)

del d3
print("del d3: ")
print("d3 deleted")

