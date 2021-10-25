import ipaddress
import socket
import struct

from datetime import datetime, timedelta
from array import  array

MAX_QUOTES_PER_MESSAGE = 50
MICROS_PER_SECOND = 1_000_000

PUBLISHER_ADDRESS = ('localhost', '50403')
addr = '127.0.0.1'
port = int(PUBLISHER_ADDRESS[1])
addr_bytes = socket.inet_aton(addr)
port_bytes = port.to_bytes(2, 'big')

print(addr_bytes)
print(port_bytes)
print("listener address in bytes", addr_bytes + port_bytes)


def serialize_address(host: str, port: int) -> bytes:
    p = array('H', [port])
    p.byteswap()
    ip = []
    for d in host.split('.'):
        ip.append(int(d))
    h = array('B', ip)
    return b''.join([h.tobytes(), p.tobytes()])

def deserialize_price(data: bytes, little_endian=True) -> float:
    # if little_endian:
    #     return int.from_bytes(data, 'little')
    # return int.from_bytes(data, 'big')
    if little_endian:
        return struct.unpack('<d', data)[0]
    return struct.unpack('>d', data)[0]

print('deserialize price: ', deserialize_price(b'\x05\x04\x03\x02\x01\xff?C'))


def serialize_utcdatetime(utc: datetime) -> bytes:
    """
    Convert a UTC datetime into a byte stream for a Forex Provider message.
    A 64-bit integer number of microseconds that have passed since 00:00:00 UTC on 1 January 1970
    (excluding leap seconds). Sent in big-endian network format.

    >>> serialize_utcdatetime(datetime(1971, 12, 10, 1, 2, 3, 64000))
    b'\\x00\\x007\\xa3e\\x8e\\xf2\\xc0'

    :param utc: timestamp to convert to desired byte format
    :return: 8-byte stream
    """
    epoch = datetime(1970, 1, 1)
    micros = (utc - epoch).total_seconds() * MICROS_PER_SECOND
    print("\tmicro-seconds elapse: ", micros)
    a = array('Q', [int(micros)])
    print("\tarray(micro-seconds): ", a)

    a.byteswap()  # convert to big-endian
    print("\tafter converting to big endian: ", a)

    return a.tobytes()

print("result in bytes to represent micro-seconds elapses since 1 January 1970: ", serialize_utcdatetime(datetime(1971, 12, 10, 1, 2, 3, 64000)))

def deserialize_utcdatetime(data: bytes) -> datetime:
    micros = int.from_bytes(data, 'big')
    return datetime(1970, 1, 1) + timedelta(microseconds=micros)

dt_now = datetime.utcnow()
print("datetime now: ", dt_now)

result = serialize_utcdatetime(dt_now)
print("result in bytes to represent micro-seconds elapses since 1 January 1970: ", result)
print("micro-seconds elapses since 1 January 1970: ", deserialize_utcdatetime(result))


currencies = (b'USD', b'CAD', b'GBP')
print("expect b'CAD': ", currencies[1])