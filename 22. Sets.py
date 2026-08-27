# Sets are unordered collection of data items. 
# They store multiple items in a single variable. 
# Set items are separated by commas and enclosed within curly brackets {}. 
# Sets are unchangeable, meaning you cannot change items of the set once created. 
# Sets do not contain duplicate items.


info={"Arpita",12,23.4,False}
print(info)

# Quick Quiz: Try to create an empty set. 
    # Check using the type() function whether the type of your variable is a set
a={}
h={12}
d={"A":12}
print(type(a))
print(type(h))
print(type(d))

# --> print the value within the set.
# --->it will print in random pattern from the the set 
# cuz set is unordered
for i in info:
    print(i)