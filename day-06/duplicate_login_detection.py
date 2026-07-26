users=["admin","john","john","alice","admin","lahari"]
duplicate=[]
seen=[]
for i in users:
    if i in seen:
        if i not in duplicate:
            duplicate.append(i)
    else:
        seen.append(i)
print(duplicate)