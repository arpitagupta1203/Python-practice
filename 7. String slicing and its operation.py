# to find the length of a function
#indexing of a word
#   M    A    N    G    O
#   0    1    2    3    4 
#  -5   -4   -3   -2   -1


a="Mango"
length=len(a)
print("The number of words in mango is: ",length)
# print("The number of words in Arpita is: ",len("Arpita"))  #error

b="Arpita"
print("b[0:3]: ",b[0:3]) #goes till 2nd position
print("b[:]: ",b[:]) #print the complete string
print("b[:3]",b[:3]) #starts from inital to 2nd one
print("b[0:len(b)-3]",b[0:len(b)-3]) #
print("b[:-3]",b[:-3]) #
print("b[-1:-3",b[-1:-3]) #no output
print("b[0:6]",b[0:6])
print("b[5:1]",b[5:1])
print("b[-4:-2]",b[-4:-2])

print(b[-2:-5])
print(b[::1])
print(b[0:6:1])  
print(b[0:6:2])   #go till last letter and skip every 2 letter
print(b[::-1])
print(b[::-2])
