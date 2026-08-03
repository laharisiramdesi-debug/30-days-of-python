sent=input("enter sentence:")
list1=sent.split()
new_list={}
for i in list1:
    if i not in new_list:
        new_list[i]=1
    else:
        new_list[i]+=1
for i in new_list:
    print(i,":",new_list[i])
