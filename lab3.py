import pickle

import sys

BUF_SZ = 4096  # tcp receive buffer size
PUBLISHER_ADDRESS = ('localhost', 50403)

# print('starting up on {} port {}'.format(*PUBLISHER_ADDRESS))

class Lab3: 

	def __init__():
		self.publisher_address = PUBLISHER_ADDRESS
		self.host = PUBLISHER_ADDRESS[0]
		self.port = int(PUBLISHER_ADDRESS[1])
		self.timeout = 5 # seconds

	def subsribe():
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
			sock.bind(publisher_address)
			print('---------------------------------------')
            print('Listening to Publisher:  {}'.format(publisher_address))
			while True: 
				print('\nblocking, waiting to receive message')
        		data = sock.recv(BUF_SZ)

        		print('received {} bytes'.format(len(data)))
        		print(data)


if _name_ == '__main__': 
	print('=======================================')
    print('Lab3 client solution starting')
	la3 = Lab3()
	print('=======================================')
    print('Lab1 client solution done, exiting.')