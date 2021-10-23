import socket
import sys

BUF_SZ = 4096  # tcp receive buffer size
# PUBLISHER_ADDRESS = ('localhost', 50403)
PUBLISHER_ADDRESS = ('127.0.0.1', 21212)

# print('starting up on {} port {}'.format(*PUBLISHER_ADDRESS))

class Lab3:

    def __init__(self):
        self.publisher_address = PUBLISHER_ADDRESS
        self.publisher_ip = PUBLISHER_ADDRESS[0]
        self.port = int(PUBLISHER_ADDRESS[1])
        self.timeout = 5  # seconds
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    def subscribe(self):

        print("Sending Subscription Message to the Publisher")
        self.sender.connect(self.publisher_address)
        ip_bytes = socket.inet_aton(self.publisher_ip)
        port_bytes = self.port.to_bytes(2, 'big')
        self.sender.sendall(ip_bytes + port_bytes)

    def subscribe2(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            print("Sending Subscription Message to the Publisher")
            sock.connect(self.publisher_address)
            ip_bytes = socket.inet_aton(self.publisher_ip)
            port_bytes = self.port.to_bytes(2, 'big')
            sock.sendall(ip_bytes + port_bytes)

    def read(self):

        self.listener.bind(self.publisher_address)
        print('---------------------------------------')
        #  print('Listening to Publisher:  {}'.format(publisher_address))
        while True:
            print('\nblocking, waiting to receive message')
            data = self.listener.recv(BUF_SZ)

            print('received {} bytes'.format(len(data)))
            print(data)

    def read2(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.bind(self.publisher_address)
            print('---------------------------------------')
            #  print('Listening to Publisher:  {}'.format(publisher_address))
            while True:
                print('\nblocking, waiting to receive message')
                data = sock.recv(BUF_SZ)

                print('received {} bytes'.format(len(data)))
                print(data)


if __name__ == '__main__':
    print("testing lab3 subscriber")
    lab3 = Lab3()
    lab3.subscribe()
    lab3.read()

    exit(1)
