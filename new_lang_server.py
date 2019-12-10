import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def create_socket():
    print('Creating socket')
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def bind():
    host = input('Type hostname: ')
    port = int(input('Type port: '))
    s.bind(host, port)
    print('Binded socket')


def listen():
    s.listen(10)
    print('listening...')


def accept():
    print('Got connection.')
    return s.accept()


def send():
    request = input("Type the request:")
    s.send(request.encode)
    print('Response sent')


def close():
    s.close()
    print('Session terminated')
