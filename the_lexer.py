import ply.lex as lex

# Reserved Words
reserved = {
    'create_socket': 'CREATE_SOCKET',
    'create_socket2': 'CREATE_SOCKET2',
    'connect': 'CONNECT',
    'receive': 'RECEIVE',
    'send': 'SEND',
    'request': 'REQUEST',
    'close': 'CLOSE',
    'bind': 'BIND',
    'listen': 'LISTEN',
    'accept': 'ACCEPT',
    'close2': 'CLOSE2'
}

# Tokens
tokens = ["HOST",
          "PORT",
          "IP"] + list(reserved.values())

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
