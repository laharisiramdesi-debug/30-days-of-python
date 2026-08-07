#using for loop
count=0
with open("name.txt","r") as file:
    for line in file:
        words=line.split()
        count+=len(words)
print(count)
#using read
with open("name.txt","r") as file:
    contents=file.read().split()
    words=len(contents)
print(words)