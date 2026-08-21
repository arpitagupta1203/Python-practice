l=[15,2,54,34,0,12,1,1,12,3,5,6,9,32,67,23]
print(len(l))

print("           ")
print("Sorted list: ")
l.sort()    #orr----> l.sort()---->then--->print(l)
print(l)

print("     ")
print("Append: ")
l.append(354)
print(l)

print("    ")
h=[3,5,7,9,8,6,4,2,0,1]
print("Reverse: ")
h.reverse()
print(h)

print("    ")
print("Index: ")
print(l.index(12))
print(l.index(1))

print("      ")
print("Count: ")
print(l.count(12))
print(l.count(3))

print("   ")
print("Copy: ")
m = l.copy()
print("m: ",m)
print("l: ",l)

print("      ")
print("Index: ")
l.insert(3,23)
l.insert(0,123)
l.insert(6,523)

print("l: ",l)
print("m: ",m)

print("       ")
print("Extend: ")
k=[78,34,6,7,98,45]
a=[99,87,56,90]
print("Before extend(k): ",k)
print("Before extend(a): ",a)
k.extend(a)
print(k)
print(a)

print("         ")
print("Concate: ")
print(k+a)

print("          ")
print("Replacement: ")
f=[12,34,35,7,98,54]
print(f)
f[0]=13
print(f)