# finally is a block in exception handling that always executes,
# whether an exception occurs or not.

# so basically apn finally ko isly use krte hai kuki jb apn function bnare hote hai 
# tb apne jese hi code execute hoga vo break hojayega isly vo break na ho toh apn finally use krte h

a=int(input("Enter a number: "))
print(f"the table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{a} X {i} = {a*i}")
except:
    print("error!")
finally:
    print("i will always execute")