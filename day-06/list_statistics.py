#using the builtin functions 
numbers=list(map(int,input("enter 10 numbers:").split()))
print(f"sum of numbers:{sum(numbers)}")
print(f"largest of numbers:{max(numbers)}")
print(f"smallest of numbers:{min(numbers)}")
print(f"average of numbers:{sum(numbers)/len(numbers)}")
#without using the built in functions
numbers=list(map(int,input("enter 10 numbers:").split()))
sum=0
max=numbers[0]
min=numbers[0]
for i in range(len(numbers)):
    sum+=numbers[i]
    if max<numbers[i]:
        max=numbers[i]
    if min>numbers[i]:
        min=numbers[i]
    
print("sum:",sum)
print("largest number:",max)
print("smallest number:",min)
print("average:",sum/len(numbers))