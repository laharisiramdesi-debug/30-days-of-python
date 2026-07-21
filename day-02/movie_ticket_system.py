age=int(input("enter age:"))
if age<5:
    print("free ticket")
elif age>=5 and age<=17:
    print("child ticket")
elif age>=18 and age<=59:
    print("adult ticket")
else:
    print("senior citizen ticket")