import ipaddress
import socket

PUBLISHER_ADDRESS = ('localhost', 50403)
addr = '127.0.0.1'
port = int(PUBLISHER_ADDRESS[1])
print(socket.inet_aton(addr))
print(socket.inet_aton('164.107.113.18'))
print(port.to_bytes(2, 'big'))