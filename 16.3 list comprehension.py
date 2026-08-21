# Syntax:
# List = [Expression(item) for item in iterable if Condition]
# Expression: It is the item which is being iterated.
# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.
# Condition: Condition checks if the item should be added to the new list or not.

lst=["cat","bat","rat","mouse","pegion","snake","penguin","lion","tiger","leopard","fish","dog","snail","catterpiller"]
print(lst)

print("         ")
a=[i for i in lst if "a" in i]
print(a)

print("           ")
o=[i for i in lst if "o" in i]
print(o)

print("           ")
m=[i for i in lst if "m" in i]
print(m)


print("           ")

num=[i for i in range(4)]
print( num)

print("           ")

nums=[i*i for i in range(5)]
print(nums)

print("           ")

numi=[i*i for i in range(10) if i%2==0]
print(numi)
