blocked_ips={
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.3"
}
with open("blocked_ips.txt","w") as file:
    for ip in blocked_ips:
        file.write(ip+"\n")
with open("blocked_ips.txt","r") as file:
    print(file.read())