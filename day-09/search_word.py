word=input("enter word:")
with open("name.txt","r") as file:
    content=file.read()
if word in content:
    print(word,"found in the file")
else:
    print(word,"not found in the file")