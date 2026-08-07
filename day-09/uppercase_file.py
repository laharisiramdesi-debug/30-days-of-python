with open("name.txt","r") as file:
    content=file.read()
uppercase_content=content.upper()
with open("upper.txt","w") as file:
    file.write(uppercase_content)
print("contents converted to uppercase and saved successfully")
