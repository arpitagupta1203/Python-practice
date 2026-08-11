# Strings are immutable
# while using upper lower any other function 
str1 = "Hello"
str2 = "!!!HELLO!!!!"


# upper= convert letter into upper case
print(str1.upper())


# lower= convert letter into lower case
print(str2.lower())


# strip = removes white spaces
str3 ="    abc    def   "
print(str3.strip())


# rstrip = remove all the trailing character
print(str2.rstrip('!'))


# replace = replace all the occurance of the word
str4 ="this is my cake, and my pen"
print(str4.replace('my','mie'))


# split = convert the string into list
print(str4.split())


# capatalize = convert the first letter into capital letter and rest to lower case
print(str4.capitalize())


# centre = string to the centre
print(str1.center(50))


# count = count a particular charather in a string
print(str4.count("a"))


# endswith = check whether a string end with a particular character
#         = we can also check whether a particular string is in the given range or not
#        = example: "hello! my name is arpita"----> to check is present or not
#        = ("string",inital position number, final postion number) --> ("is",5,15)
print(str4.endswith("pen"))
print(str4.endswith("pen!"))



# find = The find0 method searches for the first occurrence of the given value and returns the index where it is present. 
#          If given value is absent from the string then return -1.
print(str4.find("my"))



# index =  Very similar to find but we use index when we are sure that we will find this particular word in our string
print(str4.index("is"))
# print(str4.index("is,"))  it will give substring not found


#  isalnum = string have A-Z or a-z and 0-9 
str5="asmd83484"
str6="ajhsj"
str7=85
str8="   "
str9="ASFD"

print(str5.isalnum())
print(str8.isalnum())

# isaplha = check whther string have A-Z or a-z
print(str6.isalpha())
print(str8.isalpha())


# islower - to check all character are string
print(str6.islower())
print(str8.islower())
print(str9.islower())


# isprintable :Returns True if all the values within the given string are printable, if not, then return False.
print(str6.isprintable())
print(str8.isprintable())



# isspace = return true only and only of their is white spaces 
print(str6.isspace())
print(str8.isspace())



# istitle = return true only if the each letter of a string is capitalized
str10="All the Birds"
str11="All The Birds"
str12="All The BIRDs"
print(str10.istitle())
print(str11.istitle())
print(str12.istitle())



# isupper = returns True if all the characters in the string are upper case, else it returns False.
print(str6.isupper())
print(str8.isupper())
print(str9.isupper())



# startswith= checks if the string starts with a given value. If yes then return True, else return False.
print(str10.startswith("All"))
print(str10.startswith("all"))
print(str8.startswith(" "))
print(str6.startswith("a"))



# swapcase =  Upper case are converted to lower case and lower case to upper case.
print(str6.swapcase())
print(str8.swapcase())



# title = capitalize each letter of string
print(str6.title())
print(str8.title())