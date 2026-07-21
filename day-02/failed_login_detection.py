attempts=int(input("enter no. of failed login attempts:"))
if attempts < 3:
    print("normal")
elif attempts >=3 and attempts<=4:
    print("warning")
else:
    print("account locked")
