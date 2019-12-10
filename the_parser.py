import ply.yacc as yacc
import the_lexer


tokens = the_lexer.tokens


# Parsing Rules
def p_statement(p):
    """
    statement : create_socket
            / create_socket2
            / connect
            / receive
            / send
            / request
            / close
            / bind
            / listen
            / accept
            /close2

    """
    p[0] = p[1]
    pass


def p_create_socket(p):
    """
    connect : CLIENT CREATE SOCKET PHRASE
    """
    new_lang_client.create_socket(p[2])


def p_create_socket2(p):
    """
    connect : SERVER CREATE SOCKET PHRASE
    """
    new_lang_server.create_socket2(p[2])


def p_connect(p):
    """
    connect : CONNECT PHRASE
    """
    new_lang_client.connect(p[2])


def p_receive(p):
    """
    receive : CLIENT RECEIVE PHRASE
    """
    new_lang.receive(p[2], p[3])


def p_send(p):
    """
    send : CLIENT SEND PHRASE
    """
    new_lang.send(p[2], p[3])


def p_request(p):
    """
    request : CLIENT REQUEST PHRASE
    """
    new_lang.request(p[2], p[3])


def p_close(p):
    """
    close : CLIENT CLOSE PHRASE
    """
    new_lang_client.close(p[2])


def p_bind(p):
    """
    bind : SERVER BIND PHRASE
    """
    new_lang_server.bind(p[2])


def p_listen(p):
    """
    listen : SERVER LISTEN PHRASE
    """
    new_lang_server.listen(p[2])


def p_accept(p):
    """
    connect : SERVER ACCEPT PHRASE
    """
    new_lang_server.accept(p[2])


def p_close2(p):
    """
    close2 : SERVER CLOSE2 PHRASE
    """
    new_lang_server.close2(p[2])


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


parser = yacc.yacc()
while 1:
    try:
        s = input('AA2 > ')
    except EOFError:
        break
    if not s:
        continue
    elif s == 'exit':
        break
    try:
        parser.parse(s)
    except SyntaxError:
        print('Invalid syntax')