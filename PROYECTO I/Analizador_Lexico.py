import ply.lex as lex
import datetime
import subprocess


reserved = {'if': 'IF', 'else': 'ELSE', 'while': 'WHILE', 'for': 'FOR', 'input': 'INPUT', 'print':'PRINT'}

# List of token names.   This is always required
tokens = (
             'NUMBER',
             'PLUS',
             'MINUS',
             'TIMES',
             'DIVIDE',
             'LPAREN',
             'RPAREN',
             'VARIABLE',
             'HASH',
             'FLOAT'
         ) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_HASH = r'\#'




def t_FLOAT(t):
    r'[+-]?([0-9]*[.])?[0-9]+'
    t.type = reserved.get(t.value, 'FLOAT')
    return t


def t_VARIABLE(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    error_msg = f"Illegal character '{t.value[0]}'"
    log_error(error_msg)  # log the error
    t.lexer.skip(1)

# Find git user for filename
def get_git_user():
    try:
        user_name = subprocess.check_output(['git', 'config', '--get', 'user.name']).strip().decode()
        return user_name
    except subprocess.CalledProcessError:
        return 'unknown_user'

def generate_log_filename():
    now = datetime.datetime.now()
    user_git = get_git_user()  # Obtener el nombre del usuario de Git
    return f"logs/lexico-{user_git}-{now.strftime('%d%m%Y-%Hh%M')}.txt"

# Register tokens in file
def log_token(token):
    with open(log_filename, 'a') as log_file:
        log_file.write(f"Token: {token.type}, Value: {token.value}, Line: {token.lineno}\n")

def log_error(error_msg):
    with open(log_filename, 'a') as log_file:
        log_file.write(f"ERROR: {error_msg}\n")

# Build the lexer
lexer = lex.lex()

data = '''
3 + 4 * 10
  + -20 *2 If print(4) 4.3 # input(t)
'''

# Give the lexer some input
lexer.input(data)

# Generate log file
log_filename = generate_log_filename()

# Write header in log file
with open(log_filename, 'w') as log_file:
    log_file.write(f"Lex-analizer started at: {datetime.datetime.now()}\n\n")

lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    log_token(tok)

with open(log_filename, 'a') as log_file:
    log_file.write(f"\nLex-analizer finished at: {datetime.datetime.now()}\n")