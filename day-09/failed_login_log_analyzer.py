count=0
with open("failed_login.txt","r") as file:
    content=file.read()
    for line in content.split(","):
        if "failed" in line:
            count+=1
print(count)