import ply.lex as lex

# Reserved Words
reserved = {'create_client': 'CREATE_CLIENT',
    'create_server': 'CREATE_SERVER',
    'connect': 'CONNECT',
    'receive': 'RECEIVE',
    'send': 'SEND',
    'client_close': 'CLIENT_CLOSE',
    'bind': 'BIND',
    'listen': 'LISTEN',
    'accept': 'ACCEPT',
    'server_close': 'SERVER_CLOSE',
}

# Tokens
tokens = [] + list(reserved.values())

# Regular Expressions
t_ignore = '\t'


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
