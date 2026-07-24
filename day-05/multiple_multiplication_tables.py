def tables(num):
    for j in range(1,num+1):
        print(f"Table of {j}:")
        for i in range(1,num+1):
            print(f"{j}*{i}={j*i}")
        print()
n=int(input("enter number:"))
tables(n)