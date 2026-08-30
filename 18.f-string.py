about="Hey! My name is {} and I m from {}"
name="Arpita"
country="India"
print(about.format(name,country))

ab="Hey! My name is {1} and I am from {0}"
name="Anjali"
country="India"
print(ab.format(country,name))

# f-string
mine="I m {} nd from {}"
name="Yash"
country = "India"
print(f"Hey! My name is {name} and I am from {country}")




a=input("Enter a number: ")
print(f"the multi. table of {a} is:")
for i in range(1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")