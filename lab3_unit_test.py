import ipaddress
import socket
import struct

from array import  array


PUBLISHER_ADDRESS = ('localhost', '50403')
addr = '127.0.0.1'
port = int(PUBLISHER_ADDRESS[1])
addr_bytes = socket.inet_aton(addr)
port_bytes = port.to_bytes(2, 'big')

print(addr_bytes)
print(port_bytes)
print(addr_bytes + port_bytes)


def serialize_address(host: str, port: int) -> bytes:
    p = array('H', [port])
    p.byteswap()
    ip = []
    for d in host.split('.'):
        ip.append(int(d))
    h = array('B', ip)
    return b''.join([h.tobytes(), p.tobytes()])

def deserialize_price(data, little_endian  =  True):
    if little_endian:
        return struct.unpack('<d', data)
    return struct.unpack('>d', data)

print( serialize_address(addr, int(PUBLISHER_ADDRESS[1])) )
print("converting 8 bytes data to a float number: ")

