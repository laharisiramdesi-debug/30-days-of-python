#storing an ip adress and printing it
ip_address="192.37.28.7"
print(ip_address)
#store username and password and print their datatypes
username=input("username:")
password=input("password:")
print(type(username))
print(type(password))
#storing portnumbers and print it
ports=(80,443,22)
print(ports)
#store url and check whether "https" is present in it using the in operator
url="https://www.google.com"
print("https" in url)
#store a filename "report.pdf" and check whether ".pdf" is present
filename="report.pdf"
print(".pdf" in filename)
#store domain name and print its type
domain="google.com"
print(domain)
print(type(domain))
#store mac address as a string
mac_adress="00:1A:2B:3C:4D:5E"
print(mac_adress)
print(type(mac_adress))
#compare two ip address strings using ==
ip1="192.168.1.1"
ip2="192.168.1.1"
print(ip1==ip2)
#check whether admin is present in a username
username=input("enter username:")
print("admin" in username)
#create a website name,port number,protocol and print them together
website="google.com"
port=443
protocol="HTTPS"
print(website)
print(port)
print(protocol)