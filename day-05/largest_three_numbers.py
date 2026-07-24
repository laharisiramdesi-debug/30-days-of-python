def largest(a,b,c):
    if a>b and a>c:
        print(f"{a} is largest number")
    elif a<c:
        print(f"{c} is largest number")
    else:
        print(f"{b} is largest number")
a1=int(input("enter a:"))
b2=int(input("enter b:"))
c3=int(input("enter c:"))
largest(a1,b2,c3)
