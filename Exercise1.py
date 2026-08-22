import time
times=int(time.strftime('%H'))
print(times)
t=int(input("Enter the hour: "))
if(t>=0 and t<12):
    print("Good morning!  ")
elif(t>=12 and t<17):
    print("good afternoon! ")
elif(t>=17 and t<21):
    print("Good Evening")
else:
    print("Good night")    
