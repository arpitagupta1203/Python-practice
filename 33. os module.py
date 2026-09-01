import os

# make a folder of name os module prac
# os.mkdir("os module prac")


#  Running this won't work as OS MODULE PRAC is already there

# for i in range(1,12):
#     os.mkdir(f"os module prac/data {i+1}")
    
# so to run it let's make another one


if(not os.path.exists("py")):
    os.mkdir("py")

for i in range(1, 12):
#     os.mkdir(f"py/data{i+1}")
    os.rename(f"py/data{i+1}", f"py/{i-1}. data")    
# to rename it--
