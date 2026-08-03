failed_login_list=["admin","lahari","useer","admin","admin","useer"]
new_list={}
for i in failed_login_list:
    if i in new_list:
        new_list[i]+=1
    else:
        new_list[i]=1
print("failed login count:")
for i ,count in new_list.items():
    print(i,":",count)