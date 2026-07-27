blocked_ips={"192.168.1.10","192.168.1.20"}
blocked_ips.discard("192.168.1.99")#discard without gives any error while remove gives error if element is not present
print(blocked_ips)