import socket

def create_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)