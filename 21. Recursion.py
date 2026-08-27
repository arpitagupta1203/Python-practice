# factorial
def fact(num):
    if(num==0 or num==1):
        return 1
    else:
        return num*fact(num-1)


num=int(input("Enter a number for factorial: "))
print("The factorial of",num,"is: ",fact(num))
print(fact(3))



# ------> Fabbonacci series
def fabonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fabonacci(num-1)+fabonacci(num-2)

n=int(input("Enter a number: "))
for i in range(n):
    print(fabonacci(i), end=" ")