# The enumerate function is a built-in function in Python that allows
# you to loop over a sequence (such as a list, tuple, or string) and get
# the index and value of each element in the sequence at the same time. 

# ---------->

fruit=['apple','banana','grapes','lichi','berry','orange','melon','mango']
for index,fruits in enumerate(fruit):
    print(index,fruits)
    
    
# ------------------------------->
print("                     ")
print("Names: ")
name=['Arii',"anjali",'jake','yahs','pith','mark','sam','shivi','akshu']
for index,names in enumerate(name,start=1):
    print(index,".",names)