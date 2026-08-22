# Tuples are ordered collection of data items.
# They store multiple items in a single variable. 
# Tuple items are separated by commas and enclosed within round brackets (). 
# Tuples are unchangeable meaning we can not alter them after creation.

t=(23,4,54,76,25,76,84,1,3,2,6,3)

print("Length :\n",len(t))
print("      ")

print("Complete tuple:")
print(t[:])
print(t[::])
print(t[0:])
print("          ")

print("Slicing: ")
print(t[1:7])
print(t[7:1])
print(t[-7:-2])
print(t[-2:-7])
print(t[::3])
print(t[1:7:2])
print(t[1:7:3])
print(t[1:7:4])



print("             ")
print("Condition: ")
if 32 in t:
    print("yes 32 is in t")
else:
    print("no! 32 is not in t")


if 3 in t:
    print("yes 3 is in t")
else:
    print("no! 3 is not in t")



