logs = [
    "Failed Login",
    "Success Login",
    "Account Locked",
    "Failed Login",
    "Password Reset",
    "Failed Login"
]
new_list=[]
target=""
highest=0
for i in logs:
    count=0
    if i  not in new_list:
        new_list.append(i)
for j in new_list:
    count=0
    for k in logs:
        if j==k:
            count+=1
    print(j,":",count)

