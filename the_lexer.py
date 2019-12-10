import ply.lex as lex

# Reserved Words
reserved = {
    'connect': 'CONNECT',
    'receive': 'RECEIVE',
    'send': 'SEND',
    'request': 'REQUEST',
}

# Tokens
tokens = ["HOST",
          "PORT",
          "IP"] + list(reserved.values())

# Simple Regular Expressions
t_ignore = '\t'
t_HOST = r'(?!-)[a-z0-9]{1,63}(?<!-)$'
t_PORT = r'[\d+]{5}'
t_IP = r'[0-9]{3}' + r'.' + r'[0-9]{3}' + r'.' + r'[0-9]{3}' + r'.' + r'[0-9]{3}'


# Define a rule for reserved words
def t_ID(t):
    r"""[a-zA-Z]+_[a-zA-Z]+"""
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


def t_error(t):
    print('Illegal character %s', t.value[0])
    t.lexer.skip(1)
    return t


# Build the lexer
lexer = lex.lex()
