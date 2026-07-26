num=list(map(int,input("enter numbers:").split()))
ecount=0
ocount=0
for i in range(len(num)):
    if num[i]%2 ==0:
        ecount+=1
    else:
        ocount+=1
print("count of even numbers:",ecount)
print("count of odd numbers:",ocount)
