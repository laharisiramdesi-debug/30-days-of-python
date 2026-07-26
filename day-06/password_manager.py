passwds=[]
while True:
    print("1.Add password")
    print("2.View passwords")
    print("3.delete password")
    print("4.exit")
    choice=int(input("enter choice:"))
    if choice==1:
        print("Add Password:")
        passwd=input("enter new password:")
        passwds.append(passwd)
    elif choice==2:
        print("View Passwords:")
        print(passwds)
    elif choice==3:
        print("delete password:")
        passwd=input("enter password to delete:")
        if passwd in passwds:
            passwds.remove(passwd)
        else:
            print("password is not there")
    elif choice==4:
        print("exit")
        break
    else:
        print("invalid choice")