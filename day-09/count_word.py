word=input("enter word:")
count=0
with open("name.txt","r") as file:
    content=file.read()
if word in content:
    count+=1
else:
    print("word not found")
print(count)