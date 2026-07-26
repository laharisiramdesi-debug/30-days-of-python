lists=list(input("enter list:").split())
new_list=[]
for i in list:
    if i not in new_list:
        new_list.append(i)
print("new_list:",new_list)