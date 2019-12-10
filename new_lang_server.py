import socket

def create_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def bind(s, host, port):
    s.bind(host, port)

def listen(s):
    s.listen(10)

def accept(s):
    return s.accept()

def close(s):
    s.close()