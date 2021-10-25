import socket
import struct
from datetime import datetime, timedelta

BUF_SZ = 4096  # tcp receive buffer size
PUBLISHER_ADDRESS = ('127.0.0.1', 21212)
MICROS_PER_SECOND = 1_000_000
NUM_CURRENCY = 7
DEFAULT_RATE = 0

class Lab3:
    def __init__(self):
        self.publisher_address = PUBLISHER_ADDRESS
        self.publisher_ip = PUBLISHER_ADDRESS[0]
        self.publisher_port = int(PUBLISHER_ADDRESS[1])

        self.sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.listener, self.listener_address = self.start_a_listener()
        self.listener_ip, self.listener_port = self.listener_address

        self.timeout = 5  # seconds
        self.rate_dict = [[]]
        for row in range(NUM_CURRENCY):
            for col in range(NUM_CURRENCY):
                self.rate_dict[row][col] = (DEFAULT_RATE, False)
        self.currencies = ()
    def subscribe(self):
        print("Sending Subscription Message to the Publisher")
        # self.sender.connect(self.publisher_address)

        # serialize the listener address
        data = self.serialize_address(self.listener_ip, self.listener_port)
        print("sending bytes: ", data)
        send = self.sender.sendto(data, self.publisher_address)

    def read(self):
        print('---------------------------------------')
        print('Listening to Publisher:  {}'.format(self.publisher_address))
        while True:
            data = self.receive(self.listener)
            byte_len = len(data)
            start = 0
            end = 32
            while end <= byte_len:
                self.unmarshal_message(data, start)
                start = end
                end = end + 32

    def unmarshal_message(self, data: bytes, start):
        print("Datetime: ", self.deserialize_utcdatetime(data[start:start + 8]))
        print("Currency: ", data[start + 8: start + 11], "/", data[start + 11:start + 14],
              " Price: ", self.deserialize_price(data[start + 14:start + 22]), "\n")

    @staticmethod
    def start_a_listener():
        """
            Start a socket bound to 'localhost' at a random port.

            :return: listening socket and its address
        """
        print("initializing a listener")
        listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(type(listener))
        listener.bind(('localhost', 0))  # use any free socket
        # listener.listen(1)  # set it for 1
        # listener.setblocking(False)
        return listener, listener.getsockname()

    @staticmethod
    def receive(listener, buffer_size = BUF_SZ):
        """
        Receives an incoming message from the given socket.

        :param listener: socket to recv
        :param buffer_size: buffer size of socket.recv
        :return: the de-serialized data received from publisher
        :raises: whatever socket.recv or pickle.loads could raise
        """
        print('\nblocking, waiting to receive message')
        data = listener.recv(BUF_SZ)
        if not data:
            raise ValueError('socket closed')
        print('received {} bytes'.format(len(data)))
        return data

    @staticmethod
    def deserialize_price(data: bytes, little_endian=True) -> float:
        if little_endian:
            return struct.unpack('<d', data)[0]
        return struct.unpack('>d', data)[0]

    @staticmethod
    def deserialize_utcdatetime(data: bytes) -> datetime:
        micros = int.from_bytes(data, 'big')
        return datetime(1970, 1, 1) + timedelta(microseconds=micros)

    @staticmethod
    def serialize_address(ip, port) -> bytes:
        ip_bytes = socket.inet_aton(ip)
        port_bytes = port.to_bytes(2, 'big')
        return ip_bytes + port_bytes


if __name__ == '__main__':
    print("testing lab3 subscriber")
    lab3 = Lab3()
    lab3.subscribe()
    lab3.read()
    exit(1)
