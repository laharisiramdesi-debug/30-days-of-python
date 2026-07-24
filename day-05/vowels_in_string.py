def count(s):
    v="aeiou"
    count=0
    for i in s:
        if i in v:
            count+=1
    print(count)
string=input("enter string:").lower()
count(string)