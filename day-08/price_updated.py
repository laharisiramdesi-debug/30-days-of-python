products={}
n=int(input("enter no. of products:"))
for i in range(n):
    product=input("enter product:")
    price=int(input("enter price:"))
    products[product]=price
print("original prices:")
for i in products.values():
    print(product,":",i)
print("updated prices:")
for i in products.values():
    i+=(i*10/100)
    print(product,":",i)