import ply.yacc as yacc
import new_lang_server
import new_lang_client
import the_lexer
import socket

tokens = the_lexer.tokens

ids = {}
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('', 0)

# Parsing Rules
def p_statement(p):
    """
    statement : create_client
            | create_server
            | connect
            | receive
            | send
            | client_close
            | bind
            | listen
            | accept
            | server_close
            | error
    """


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


def p_create_client(p):
    'create_client : CREATE_CLIENT'
    new_lang_client.create_socket()


def p_create_server(p):
    'create_server : CREATE_SERVER'
    new_lang_server.create_socket()


def p_connect(p):
    'connect : CONNECT'
    new_lang_client.connect(client_socket)


def p_receive(p):
    'receive : RECEIVE'
    new_lang_client.receive(client_socket)


def p_send(p):
    'send : SEND'
    new_lang_server.send(conn)


def p_client_close(p):
    'client_close : CLIENT_CLOSE'
    new_lang_client.close(client_socket)


def p_bind(p):
    'bind : BIND'
    new_lang_server.bind(server_socket)


def p_listen(p):
    'listen : LISTEN'
    new_lang_server.listen(server_socket)


def p_accept(p):
    'accept : ACCEPT'
    return new_lang_server.accept(server_socket)


def p_server_close(p):
    'server_close : SERVER_CLOSE'
    new_lang_server.close(server_socket)


yacc.yacc()
while True:
    s = input('AA2 > ')
    if s == 'create_client':
        p_create_client(client_socket)
    elif s == 'create_server':
        p_create_server(server_socket)
    elif s == 'bind':
        p_bind(server_socket)
    elif s == 'listen':
        p_listen(server_socket)
    elif s == 'connect':
        p_connect(client_socket)
    elif s == 'accept':
        conn, address = p_accept(server_socket)
    elif s == 'send':
        p_send(conn)
    elif s == 'receive':
        p_receive(client_socket)
    elif s == 'client_close':
        p_client_close(client_socket)
    elif s == 'server_close':
        p_server_close(server_socket)