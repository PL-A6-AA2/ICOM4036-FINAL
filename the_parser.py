import ply.yacc as yacc
import new_lang_server
import new_lang_client
import the_lexer

tokens = the_lexer.tokens

ids = {}


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
            | host
            | port
            | ip

    """
    # | request <--- esto va arriba como los demas


def p_host(p):
    'host : HOST'
    p[0] = p[12]


def p_port(p):
    'port : PORT'
    p[0] = p[13]


def p_ip(p):
    'ip : IP'
    p[0] = p[14]


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


def p_create_client_socket(p):
    'create_client_socket : CREATE_CLIENT_SOCKET'
    new_lang_client.create_socket()


def p_create_server_socket(p):
    'create_server_socket : CREATE_SERVER_SOCKET'
    new_lang_server.create_socket()


def p_connect(p):
    'connect : CONNECT'
    new_lang_client.connect(p[12], p[13])


def p_receive(p):
    'receive : RECEIVE'
    new_lang.receive(p[12])


def p_send(p):
    'send : SEND'
    new_lang_server.send('Succesfully connected')


def p_client_close(p):
    'client_close : CLIENT_CLOSE'
    new_lang_client.close()


def p_bind(p):
    'bind : BIND'
    new_lang_server.bind(p[12], p[13])


def p_listen(p):
    'listen : LISTEN'
    new_lang_server.listen(10)


def p_accept(p):
    'accept : ACCEPT'
    new_lang_server.accept()


def p_server_close(p):
    'server_close : SERVER_CLOSE'
    new_lang_server.close()

#def p_request(p):
  #      'request : REQUEST'
   #     new_lang_request()


yacc.yacc()
while True:
    try:
        s = input('AA2 > ')
    except EOFError:
        break
    yacc.parse(s)
