# Exception handling is used to handle errors that occur while a program is running, 
# so that the program doesn't suddenly stop.

# try....except
a=input("Enter a number: ")
print(f"the table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")

except Exception as e:
    print(e)
    
print("code completed!")


# ---X--------X-------X-------X------X------X-----X------X------X-----X-----X-----X-----X----

# Try except
c=input("Enter a number: ")
print(f"the table of {c}: ")

try:
    for i in range(1,11):
        print(f"{int(c)} X {i} = {int(c)*i}")    
except:
    print("Invalid syntax")
        
print("yo! code done..........!!tada")