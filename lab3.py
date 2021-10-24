import socket
import sys
import struct

BUF_SZ = 4096  # tcp receive buffer size
# PUBLISHER_ADDRESS = ('localhost', 50403)
PUBLISHER_ADDRESS = ('127.0.0.1', 21212)

# print('starting up on {} port {}'.format(*PUBLISHER_ADDRESS))

class Lab3:

    def __init__(self):

        self.publisher_address = PUBLISHER_ADDRESS
        self.publisher_ip = PUBLISHER_ADDRESS[0]
        self.publisher_port = int(PUBLISHER_ADDRESS[1])

        self.sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.listener, self.listener_address = self.start_a_listener()
        self.listener_ip, self.listener_port = self.listener_address

        self.timeout = 5  # seconds

    def subscribe(self):

        print("Sending Subscription Message to the Publisher")
        # self.sender.connect(self.publisher_address)

        # serialize the listener address
        ip_bytes = socket.inet_aton(self.listener_ip)
        port_bytes = self.listener_port.to_bytes(2, 'big')
        data = ip_bytes + port_bytes
        print("listener ip: ", self.listener_ip)
        print('listener port: ', self.listener_port)
        print("sending bytes: ", ip_bytes + port_bytes)

        send = self.sender.sendto(data, self.publisher_address)

    def read(self):
        print('---------------------------------------')
        #  print('Listening to Publisher:  {}'.format(publisher_address))
        start = 0
        end = 0
        while True:
            print('\nblocking, waiting to receive message')
            data = self.listener.recv(BUF_SZ)
            if not data:
                raise ValueError('socket closed')
            print('received {} bytes'.format(len(data)))
            end = len(data)
            print("start to deserialize: data has ", end, " bytes")
            print("Currency: ", data[8: 12], "/", data[12:14], ' Price', self.deserialize_price(data[14: 22])[0])
            # print("price in bytes: ", data[14: 22])
            # print()
            print(data)

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
        Receives and unpickles an incoming message from the given socket.

        :param listener: socket to recv
        :param buffer_size: buffer size of socket.recv
        :return: the de-serialized data received from publisher
        :raises: whatever socket.recv or pickle.loads could raise
        """
        packet = listener.recv(buffer_size)
        if not packet:
            raise ValueError('socket closed')
        return packet

    @staticmethod
    def deserialize_price(data, little_endian=True):
        if little_endian:
            return struct.unpack('<d', data)
        return struct.unpack('>d', data)

    @staticmethod
    def deserialize_utcdatetime():
        return 0

    @staticmethod
    def serialize_address():
        return 0

    @staticmethod
    def unmarshal_message():
        return -1

if __name__ == '__main__':
    print("testing lab3 subscriber")
    lab3 = Lab3()
    lab3.subscribe()
    lab3.read()
    exit(1)
