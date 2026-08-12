# default case: case_ 

a=int(input("Enter a value: "))

match a:
    case 0:
        print("The number uh enter is zero")
    
    case 4 if a%2==0:
        print("the case is 4")
        
    case _ if (a!=90):
        print(a,"The number is not 90")
        
    case _:   #default
        print(a)
        