# raise: to raise any custom error
age=int(input("Enter the age: "))
if age<8 or age>10:
    raise ValueError("you can not ride on the swing")

