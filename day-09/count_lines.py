#using readlines
with open("name.txt","r") as file:
    lines=file.readlines()
print(lines)
print("no. of lines:",len(lines))
#using for loop
count=0
with open("name.txt","r") as file:
    for line in file:
        count+=1
print("number of lines:",count)
#using sum
with open("name.txt","r") as file:
    count=sum(1 for line in file)
print("no.of lines",count)