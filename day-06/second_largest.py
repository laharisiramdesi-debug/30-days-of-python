num=list(map(int,input("enter list:").split()))
max=num[0]
smax=num[0]
for i in num:
    if max<i:
        smax=max
        max=i
    elif i>smax and i!=max:
        smax=i
print("largest number",max)
print("second largest number",smax)

