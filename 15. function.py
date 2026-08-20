# Function: Reusable block of code
# types of function:
            #built in
            # user defined

# Built-in functions:

# These functions are defined and pre-coded in python. Some
# examples of built-in functions are as follows:

# min0, max0, len0, sum0, type0, range0, dict0, list0, tuple0, set0,
# print0, etc. 


# types of arguements:-
            # Default Arguments
            # Keyword Arguments
            # Variable length Arguments
            # Required Arguments


#Without arguement:- 
def add():
    print("sum is: ",20+30)
add()

def adds(a,b):
    print("addition is: ",a+b)
adds(10,30)

def greater(a,b):
    if(a>b):
        print(a, " is greater than ",b)
    else:
        print(b, " is greater than ",a)
        
greater(30,40)
greater(89,40)


c=30
d=24
greater(c,d)
adds(c,d)

def lesser(a,b):
    pass    #it means we will continue this function later on


def name(fname="manoj",mname="kumar",lname="jain"):
    print("hello! ", fname,mname,lname)
    
name()
name("arsh")
name("ram","dev")
name("nisha","singh","jadon")