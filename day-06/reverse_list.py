#without using reverse() 
num=list(input("enter list:").split())
print("reverse of a list:",num[-1::-1])
#even without using the slicing
reversed_list=[]
for i in range(len(num)-1,-1,-1):
    reversed_list.append(num[i])
print(reversed_list)