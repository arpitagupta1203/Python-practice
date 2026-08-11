num=int(input("Enter any integer: "))
if(num<0):
    print(num," number is negative")
elif(num>0 and num<=10):
    print(num," number lies from 1 to 10")
    if(num>10 and num<=20):
        print(num," number lies from 11 to 20")
    elif(num>20 and num<=30):
        print(num," number lies 21 to 30")
else:
    print(num," number is greater than 30")
    
