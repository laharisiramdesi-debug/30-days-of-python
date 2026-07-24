def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    return factorial
num=int(input("enter number:"))
print(fact(num))