def even(start,end):
    for i in range(start,end+1):
        if i%2 == 0:
            print(i)
a=int(input("enter starting number:"))
b=int(input("enter ending number:"))
print("even numbers are:")
even(a,b)
