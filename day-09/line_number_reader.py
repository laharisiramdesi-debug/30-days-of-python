with open("file.txt","w") as file:
    file.write("python is easy\nlearning python")
with open("file.txt","r") as file:
    number=1
    for line in file:
        print(number,":",line.strip())
        number+=1
#using enumerate()
with open("file.txt","r") as file:
    for number,line in enumerate(file,start=1):
        print(number,":",line.strip())
