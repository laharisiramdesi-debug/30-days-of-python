failed_logins=["johhn","admin","johhn","laahri","admin","admin"]
users=[]
target=""
highest=0
print("====SOC Dashboard====")
print("total failed logins:",len(failed_logins))
for i in failed_logins:
    if i not in users:
        users.append(i)
print("unique users:",len(users))
for user in users:
    count=0
    for login in failed_logins:
        if user==login:
            count+=1
    if count>highest:
        highest=count
        target=user
print("most targeted user:",target)
if highest>=3:
    print("possible brute force:yes")
else:
    print("possible brute force:no")
