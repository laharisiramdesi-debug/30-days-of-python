usernames=[
    "lahari",
    "lahari",
    "madhu",
    "charan"
]

duplicates=set()
seen=set()

with open("username.txt","w") as file:
    for i in usernames:
        file.write(i+"\n")
        
with open("username.txt","r") as file:
    for line in file:
        username=line.strip()
        if username in seen:
            duplicates.add(username)
        else:
            seen.add(username)
print(duplicates)
            

