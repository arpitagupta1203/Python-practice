# Importing in Python is the process of loading code from a Python module into the current script.
# This allows you to use the functions and variables defined in the module in your current script, as
# well as any additional modules that the imported module may depend on.

print("sqrt: ")
import math
sq=math.sqrt(9)
print(sq)
print("     ")

# ------------>ALSO:-to import some particular math module
print("to import some particular math module: ")
from math import sqrt,pi
print(sqrt(4))
print(pi)
print("     ")

# --------> to import everything of a module
# from math import *
print("here we are using m at place of math: ")
import math as m
m.sqrt(64)
print("     ")
# here we are using m at place of math


# to look all the function of any file/module
import math
print("to look all the function of any file/module: ")
print(dir(math))
print("     ")


# another method to import
print("another method to import")
from file import arpita
arpita()
print("         ")

print("another method to import")

from file import sum as addition
addition()


