ports=[22,80,443,21,23,25,53,110,3306,8080]
for i in ports:
    print("scanning port",i,"...")
    print("open\n")
total=0
max=ports[0]
min=ports[0]
for i in ports:
    total+=i
    if max<i:
        max=i
    if min>i:
        min=i
avg = total/len(ports)
print(f"total ports:{len(ports)}")
print(f"largest port:{max}")
print(f"smallest port:{min}")
print(f"average port:{avg}")