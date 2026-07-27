ports=[80,22,80,21,443,22,53,53]
port=sorted(set(ports))
print("unique ports:")
for i in port:
    print(i)
print("total ports:",len(port))