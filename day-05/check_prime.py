def check(num):
    for i in range(1,num+1):
        count=0
        if num%i == 0:
            count+=1
    if count==2:
        print("it is a prime number")
    else:
        print("it is not a prime number")
n=int(input("enter number"))
check(n)
