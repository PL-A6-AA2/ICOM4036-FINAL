import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def create_socket():
    print('Creating socket')
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connect():
    host = input('Type hostname: ')
    port = int(input('Type port: '))
    s.connect((host, port))
    print('Established connection')


def receive():
    s.recv(4096)


def close():
    s.close()
    print('Disconnected')