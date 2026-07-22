words=input("enter word:")
repeated={}
for i in words:
    if i in repeated:
        repeated[i] += 1
    else:
        repeated[i]=1
print("character frequency:")
for i in repeated:
    print(i,":",repeated[i])