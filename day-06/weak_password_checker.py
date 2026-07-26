weak_passwds=["1233456","password","admin","qwerty","welcome"]
passwd=(input("enter password:"))
if passwd in weak_passwds:
    print("weak password")
else:
    print("strong password")