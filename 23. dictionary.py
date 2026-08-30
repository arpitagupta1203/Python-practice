# Dictionaries are ordered collection of data items. 
# They store multiple items in a single variable. 
# items are key-value pairs that are separated by commas and enclosed within curly brackets {}.


# Dictionary
info={'name':'Arpita','age':19,'vote':True,12:'Arii'}
print(info)

# accessing single value
print("             ")

print("Accessing single value:")
print("info.get(12): ",info.get(12))
print("info.get(name): ",info.get('name'))
print("info['name']: ",info['name'])

print("                 ")

# accessing multiple value

print("Accessing multiple value: ")
print("info.values(): ")
print(info.values())
print("info.keys(): ")
print(info.keys())
print("         ")


# Accessing key-value pairs:
print("Accessing key-value pairs: ")
print(info.items())




