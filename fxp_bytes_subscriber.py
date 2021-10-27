import socket
import struct
from datetime import datetime, timedelta

from BellmanFord import BellmanFord

BUF_SZ = 4096  # tcp receive buffer size
PUBLISHER_ADDRESS = ('127.0.0.1', 50403)
MICROS_PER_SECOND = 1_000_000
NUM_CURRENCY = 7
DEFAULT_RATE = 0
RATE_LIFETIME = 1.5


class Subscriber:
    def __init__(self) -> object:
        self.publisher_address = PUBLISHER_ADDRESS
        self.publisher_ip = PUBLISHER_ADDRESS[0]
        self.publisher_port = int(PUBLISHER_ADDRESS[1])

        self.sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.listener, self.listener_address = self.start_a_listener()
        self.listener_ip, self.listener_port = self.listener_address
        self.subscribe()

    def subscribe(self):
        print("Sending Subscription Message to the Publisher")
        # serialize the listener address
        data = self.serialize_address(self.listener_ip, self.listener_port)
        print("sending bytes: ", data)
        self.sender.sendto(data, self.publisher_address)

    def listener_receive(self):
        data = self.receive(self.listener)
        return data

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
    def serialize_address(ip, port) -> bytes:
        ip_bytes = socket.inet_aton(ip)
        port_bytes = port.to_bytes(2, 'big')
        return ip_bytes + port_bytes


