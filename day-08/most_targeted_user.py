failed_login_attempts=["user","admin","admin","admin","lahari"]
new_list={}
target=""
highest=0
for i in failed_login_attempts:
    if i in new_list:
        new_list[i]+=1
    else:
        new_list[i]=1
    if new_list[i]>highest:
        highest=new_list[i]
        target=i
print("most targeted user:",target,"with attempts:",highest)