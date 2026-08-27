# Docstrings are the string literals that appear right after the definition of a 
        # function, method, class or module.
#  enclosed with ('''----''')
#  to show docstring:
    # print(filename.__doc__)
    
# docstring is written just below the function if any other line is inserted between function and
    # docstring then docstring will not be printed
    

# ----> VALID DOCSTRING
def sum():
    '''take input from user and then print their sum'''
    a=int(input("enter a: "))
    b=int(input("Enter b: "))
    # return a+b -----> or
    print(a+b)

sum()
print(sum.__doc__)


# ----->INVALID DOCSTRING
def add():
    c=int(input("Enter c: "))
    '''take input from user and then print their sum'''
    a=int(input("enter a: "))
    b=int(input("Enter b: "))
    # return a+b+c -----> or
    print(a+b+c)

add()
print(add.__doc__)
