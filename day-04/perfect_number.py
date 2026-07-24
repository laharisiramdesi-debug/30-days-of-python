"""perfect number is a number whose proper divisors excluding the number
itself add up to the number"""
num=int(input("enter number:"))
total=0
for i in range(1,num):
    if num%i==0:
        total+=i
if total==num:
    print("perfect number")
else:
    print("not a perfect number")