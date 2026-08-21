# default args
def average(a=9,b=4):
    print("The average is: ",(a+b)/2)
    
average()

# keyword args :- no need to paas the values according to the order
def sum(a=8,c=83,b=5):
    print("sum is: ",a+b+c)
    
sum(c=2,a=3)
sum(b=87,c=34,a=95)
sum(b=34,a=85,c=57)
sum(29,c=23)
sum(68,86,75)
sum()
# sum(3)        -: error


# required args
def name(fname,mname,lname):
    print("hello! ",fname,mname,lname)
    
name("manoj", "kumar", "singh")

# keyword args
def num (*numbers):
    print(type(num))
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("the average of number is: ", sum/len(numbers))
        
num (1 , 2 , 3)
num(12,37,4567,435)