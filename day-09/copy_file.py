#using read()
with open("source.txt","w") as source:
    source.write("python is easy")
with open("source.txt","r") as source:
    content=source.read()
with open("destination.txt","w") as destination:
    destination.write(content)
print("file copied successfully")
with open("destination.txt","r") as destination:
    print(destination.read())
#using for loop
with open("source.txt","r") as source:
    with open("destination.txt","w") as destination:
        for line in source:
            destination.write(line)
with open("destination.txt","r") as destination:
    print(destination.read())
print("file copied successfully")
