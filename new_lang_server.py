import socket

def create_socket():
    print('Creating socket')
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def bind(s, host, port):
    s.bind(host, port)
    print('Binded socket')

def listen(s):
    s.listen(10)
    print('listening...')


def accept(s):
    print('Got connection.')
    return s.accept()

def send(connection):
    connection.send('Succesfully connected')
    print('Response sent')


def close(s):
    s.close()
    print('Session terminated')