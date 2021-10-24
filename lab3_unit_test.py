import ipaddress
import socket

PUBLISHER_ADDRESS = ('localhost', 50403)
addr = '127.0.0.1'
port = int(PUBLISHER_ADDRESS[1])
addr_bytes = socket.inet_aton(addr)
port_bytes = port.to_bytes(2, 'big')

print(addr_bytes)
print(port_bytes)
print(addr_bytes + port_bytes)
