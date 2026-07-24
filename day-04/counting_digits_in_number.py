#method 1
num=(input("enter number:"))
count=0
for i in num:
    count+=1
print(count)
#method 2
n=int(input("enter number:"))
count=0
while n>0:
    n=n//10
    count+=1
print(count)