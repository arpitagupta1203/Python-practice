# Tuples are immutable, hence if you want to add, remove or change tuple
# items, then first you must convert the tuple to a list. 
# Then perform operation on that list and convert it back to tuple.
# we can directly concate the tuple

num=(12,2,35,6,34,2,5,345,243,45,21,3)
temp=list(num)
print("Converted to list: ")
print("         ")

print("Append: ")
temp.append(92)
print(temp)
print("         ")


print("Pop: ")
temp.pop(3)   #temp.pop(index)
print(temp)
print("         ")


print("Adding anything at position(Index): ")
temp[2]=1999        #35 will be replaced by 1999
print(temp)
print("     ")

print("Sort: ")
temp.sort()
print(temp)
print("         ")


print("Back to tuple: ")
num=tuple(temp)
print(num)


