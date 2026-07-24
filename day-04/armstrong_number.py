#armstrong number is a number that is equal to the sum of its digits,
# each raised by power of the number of digits
num=int(input("enter number:"))
digits=len(str(num))
temp=num
total=0
while temp > 0:
    n=temp%10
    total += n**digits
    temp=temp//10
if total==num:
    print("armstrong number")
else:
    print("not a armstrong number")