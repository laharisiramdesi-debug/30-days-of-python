login_attempts=[
    "lahari","charan","lahari","charan","madhu","madhu","madhu"
]
print("total no. of login attempts:",len(login_attempts))
unique_users=set(login_attempts)
print("unique_users:",unique_users)
failed_login={}
for i in login_attempts:
    if i not in failed_login:
        failed_login[i]=1
    else:
        failed_login[i]+=1
print("failed login counter:",failed_login)
highest=0
target=""
for i in failed_login:
    if failed_login[i] > highest:
        highest=failed_login[i]
        target=i
print("most targeted user:",target)
found="no"
for i in failed_login:
    if failed_login[i]>=5:
        found="yes"
print("any user has 5 or more failed logins?",found)
