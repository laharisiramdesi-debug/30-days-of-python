balance=5000
amount=int(input("enter amount:"))
if amount<=0:
    print("invalid amount")
elif amount > balance:
    print("insufficient balance")
else:
    print("withdrawal successfull")