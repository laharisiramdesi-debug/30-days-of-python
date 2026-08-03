ip_frequency={}
n=int(input("enter no.of frequencies:"))
for i in range(n):
    ip=input("enter ip address:")
    attempts=int(input("enter login attempts:"))
    ip_frequency[ip]=attempts
print("IPs with more than 3 login attempts:")
for i in ip_frequency:
    if ip_frequency[i]>3:
        print(i,":",ip_frequency[i])