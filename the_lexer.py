import ply.lex as lex

# Reserved Words
reserved = {'create_client_socket': 'CREATE_CLIENT_SOCKET',
    'create_server_socket': 'CREATE_SERVER_SOCKET',
    'connect': 'CONNECT',
    'receive': 'RECEIVE',
    'send': 'SEND',
    'client_close': 'CLIENT_CLOSE',
    'bind': 'BIND',
    'listen': 'LISTEN',
    'accept': 'ACCEPT',
    'server_close': 'SERVER_CLOSE',
    'host': 'HOST',
    'port': 'PORT',
    'ip': 'IP'
    #'request: REQUEST'
}

# Tokens
tokens = [] + list(reserved.values())

# Regular Expressions
t_ignore = '\t'
t_HOST = r'(?!-)[a-zA-Z0-9]{1,63}(?<!-)$'
t_PORT = r'[\d+]{5}'
t_IP = r'[0-9]{3}' + r'.' + r'[0-9]{3}' + r'.' + r'[0-9]{3}' + r'.' + r'[0-9]{3}'


# Define a rule so we can track line numbers
def t_newline(t):
    r"""
    \n+
    """
    t.lexer.lineno += len(t.value)


def t_error(t):
    print('Illegal character %s', t.value[0])
    t.lexer.skip(1)
    return t


# Build the lexer
lexer = lex.lex()
