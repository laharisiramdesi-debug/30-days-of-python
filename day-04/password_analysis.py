password=input("enter password:")
u=0
l=0
d=0
s=0
for i in password:
    if  i.isupper():
        u+=1
    elif  i.islower():
        l+=1
    elif i.isdigit():
        d+=1
    else:
        s+=1
print(u)
print(l)
print(d)
print(s)