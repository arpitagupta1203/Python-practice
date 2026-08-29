s1={12,23,43,54,5}
s2={12,43,5}
s3={3,76,79}

# isdisjoint()------->
    # The isdisjoint() method checks if items of given set are present in another set. 
    # This method returns False if items are present, else it returns True.
    
print("Disjoint: ")
print("             ")
print("Disjoint(s1,s2): ",s1.isdisjoint(s2))
print("Disjoint (s2,s1): ",s2.isdisjoint(s1))
print("Disjoint (s3,s1): ",s3.isdisjoint(s1))
print("             ")
print("S1: ",s1,"\nS2: ",s2,"\nS3: ",s3)
print("             ")

# issuperset()----------->
    # The issuperset0 method checks if all the items of a particular set are present in the original set. 
    # It returns True if all the items are present, else it returns False.

print("issuperset: ")
print("             ")
print("issuperset(s2,s1): ",s2.issuperset(s1))
print("issuperset(s2,s1): ",s1.issuperset(s2))
print("         ")


# issubset():--------->
    #method checks if all the items of the original set are present in the particular set.
    #It returns True if all the items are present, else it returns False.
print("issubset: ")
print("             ")
print("issubset(s2,s1): ",s2.issubset(s1))
print("issubset(s1,s1): ",s1.issubset(s2))
print("         ")


#add()
    # to add single item in the set
print("before add:",s2)
s2.add(91)
print("After add: ",s2)


# update()
print("             ")
print("Update: ")
print("Before update",s1)
print("Before update",s2)
print("             ")
s1.update(s2)
print("After update: ",s1,"\nAfter update: ",s2)
print("             ")


# remove()/discard()
        # We can use remove() and discard() methods to remove items form list.
    # The main difference between remove and discard is that, if we try
    # to delete an item which is not present in set, then remove() raises
    # an error, whereas discard() does not raise any error.
print("Remove: ")    
print("S1: ",s1.remove(5))
print(s1)
print("         ")
print("Discard: ")
print("S1: ",s1.discard(43))
print(s1)



# pop()
    # This method removes the last item of the set but the catch is that
    # we don't know which item gets popped as sets are unordered.
    # However, you can access the popped item if you assign the pop() method to a variable.
print("         ")
print("Pop: ")
print("S1: ",s1)
print("Popped element is: ",s1.pop())
print(s1)
print("             ")

# del()
    # del is not a method, rather it is a keyword which deletes the set entirely.

del s1
# print(s1) won't work cuz s1 is deleted


# clear()
print("             ")
print("clear: ")
print("s2: ",s2)
s2.clear() 
print("s2:",s2)