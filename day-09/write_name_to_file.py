with open("name.txt","w") as file:
    file.write("hi")
with open("name.txt","r") as file:
    print(file.read())
with open("name.txt","a") as file:
   file.write(" lahari")
with open("name.txt","r") as file:
    print(file.read())
