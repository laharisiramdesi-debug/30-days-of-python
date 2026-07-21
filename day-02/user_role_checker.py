role=input("enter role:")
if role=="admin":
    print("full access")
elif role=="analyst":
    print("limited access")
elif role=="guest":
    print("read only access")
else:
    print("invalid role")