login_records = [
    ("admin", "192.168.1.10"),
    ("john", "192.168.1.20"),
    ("admin", "192.168.1.10"),
    ("guest", "192.168.1.30"),
    ("john", "192.168.1.20")
]
x=set(login_records)
print("===unique ip report===")
for name,ip in login_records:
    print(ip)
print("total number of unique ips:",len(x))

