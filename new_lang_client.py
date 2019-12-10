import socket


def create_socket():
    print('Creating socket')
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connect(s):
    s.connect(host, port)
    print('Established connection')


def receive(s):
    s.recv(4096)


def close(s):
    s.close()
    print('Disconnected')