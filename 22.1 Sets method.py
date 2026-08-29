s1={1,3,5}
s2={2,4,5,6,8}
s3={9,5,6,23,12}
s4={1,2,3,4,8}
s5={3,4,7,8,5}
print("s1: ",s1)
print("s2: ",s2)
print("s3: ",s3)
print("s4: ",s4)
print("s5: ",s5)
print("             ")

# ----------->union() and update():
# union()
print("Union(of s1 and s2): ",s1.union(s2))

# update
s3.update(s2)   #this means s1 m vo values le aao jo s2 m nhi hai
print("Update(of s3 and s2): ",s3)
print("         ")


print("s1: ",s1)
print("s2: ",s2)
print("s3: ",s3)
print("s4: ",s4)
print("s5: ",s5)
print("             ")



# ----> intersection and intersection_update()

print("Intersection(of s1 and s2): ",s1.intersection(s2))

s4.intersection_update(s2)
print("Intersection update(of s4 and s2): ",s4)
print("         ")


print("s1: ",s1)
print("s2: ",s2)
print("s3: ",s3)
print("s4: ",s4)
print("s5: ",s5)
print("             ")


# ------>Symmetric_difference and symmetric_difference_update():
    # esi values jo dono set m common hai unhe remove krke jo values bachi hai

print("Symmetric_diff(of s2 and s4): ",s2.symmetric_difference(s4))
        # S2 and S4 ki common value ko remove krke S2 ki values dena
        
s5.symmetric_difference_update(s4)
print("Symmetric_difference_update(of s5 and s4): ",s5)
print("         ")


print("s1: ",s1)
print("s2: ",s2)
print("s3: ",s3)
print("s4: ",s4)
print("s5: ",s5)
print("             ")


# ------->difference() and difference_update():
# it is basically A-B:  where:-
    # values of B are removed from A vice versa in B-A
    
print("Difference (of s2 and s4): ",s2.difference(s4))

print("             ")
print("s1: ",s1)
print("s2: ",s2)
print("s3: ",s3)
print("s4: ",s4)
print("s5: ",s5)

print("             ")
print("Difference_update (of s1 and s5): ",s1.difference_update(s5))

print("             ")

print("s1: ",s1)
print("s2: ",s2)
print("s3: ",s3)
print("s4: ",s4)
print("s5: ",s5)
print("             ")

