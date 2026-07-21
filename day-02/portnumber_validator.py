portnumber=int(input("enter port number:"))
if portnumber>=1 and portnumber<=65535:
    print("valid port")
else:
    print("invalid port")