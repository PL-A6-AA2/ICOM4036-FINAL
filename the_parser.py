import ply.yacc as yacc
import new_lang_server
import new_lang_client
import the_lexer
import socket

tokens = the_lexer.tokens

ids = {}
p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Parsing Rules
def p_statement(p):
    """
    statement : create_client_socket
            | create_server_socket
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
    # | request <--- esto va arriba como los demas


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


def p_create_client_socket():
    'create_client_socket : CREATE_CLIENT_SOCKET'
    new_lang_client.create_socket()


def p_create_server_socket():
    'create_server_socket : CREATE_SERVER_SOCKET'
    new_lang_server.create_socket()


def p_connect():
    'connect : CONNECT'
    new_lang_client.connect()


def p_receive():
    'receive : RECEIVE'
    new_lang.receive()


def p_send():
    'send : SEND'
    new_lang_server.send()


def p_client_close():
    'client_close : CLIENT_CLOSE'
    new_lang_client.close()


def p_bind():
    'bind : BIND'
    new_lang_server.bind()


def p_listen():
    'listen : LISTEN'
    new_lang_server.listen()


def p_accept():
    'accept : ACCEPT'
    new_lang_server.accept()


def p_server_close():
    'server_close : SERVER_CLOSE'
    new_lang_server.close()


# def p_request(p):
#      'request : REQUEST'
#     new_lang_request()


yacc.yacc()
while True:
    s = input('AA2 > ')
    if s == 'create_client_socket':
        p_create_client_socket()
    elif s == 'create_server_socket':
        p_create_server_socket()
    elif s == 'connect':
        p_connect()
    elif s == 'receive': #
        p_receive()
    elif s == 'send': #
        p_send()
    elif s == 'client_close':
        p_client_close()
    elif s == 'bind': #
        p_bind()
    elif s == 'listen': #
        p_listen()
    elif s == 'accept': #
        p_accept()
    elif s == 'server_close':
        p_server_close()