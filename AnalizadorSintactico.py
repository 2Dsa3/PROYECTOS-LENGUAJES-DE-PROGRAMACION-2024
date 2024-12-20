import ply.yacc as yacc
from AnalizadorLexico import tokens, generate_log_filename
import datetime

#TODO: lo comentado
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NEGATION'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULE'),
)

# Definición de las reglas del analizador
def p_program(p):
    """program : main_func"""
    p[0] = ('program', p[1])

def p_main_func(p):
    """main_func : VOID MAIN LPAREN RPAREN LBRACE statements RBRACE"""
    p[0] = ('main', p[6])


def p_statements(p):
    """statements : statements statement
                  | statement"""
    if len(p) == 3:
        p[0] = ('statements', p[1], p[2])
    else:
        p[0] = ('statement', p[1])


#  TODO Agregar aqui mas formas de statement
def p_statement(p):
    """statement : var_declaration SEMICOLON"""
    p[0] = ('statement', p[1])


# Reglas para var_declaration
def p_var_declaration(p):
    """var_declaration : type VARIABLE ASSIGN value
                       | type VARIABLE ASSIGN bool_expression
                       | type VARIABLE ASSIGN num_expression
                       | type VARIABLE ASSIGN data_structure
                       | type VARIABLE"""
    if len(p) == 5:
        p[0] = ('var_declaration_with_value', p[1], p[2], p[4])
    else:
        p[0] = ('var_declaration_without_value', p[1], p[2])


def p_type(p):
    """type : STRING
            | LIST
            | SET
            | MAP
            | STACK
            | QUEUE
            | TREE
            | GRAPH
            | DOUBLE
            | INTEGER
            | BOOL
            | VAR_TYPE"""
    p[0] = p[1]

# Reglas para las expresiones
def p_value(p):
    # TODO add more values over time
    """value : STRING_LITERAL
             | NUMBER
             | FLOAT
             | TRUE
             | FALSE"""
    p[0] = p[1]

def p_num_expression_binop(p):
    """num_expression : num_expression PLUS num_expression
                      | num_expression MINUS num_expression
                      | num_expression TIMES num_expression
                      | num_expression DIVIDE num_expression
                      | num_expression MODULE num_expression
                      | LPAREN num_expression RPAREN"""
    p[0] = ('binop', p[1], p[2], p[3])

def p_num_expression_value(p):
    """num_expression : NUMBER
                      | FLOAT"""
    p[0] = ('num_value', p[1])

# Reglas para expresiones booleanas
def p_bool_expression_binop(p):
    """bool_expression : bool_expression AND bool_expression
                       | bool_expression OR bool_expression"""
    p[0] = ('bool_binop', p[2], p[1], p[3])

def p_bool_expression_negation(p):
    """bool_expression : NEGATION bool_expression"""
    p[0] = ('bool_negation', p[2])

def p_bool_expression_value(p):
    """bool_expression : TRUE
                       | FALSE"""
    p[0] = ('bool_value', p[1])

# Reglas para estructuras de datos
def p_data_structure(p):
    """data_structure : list_structure
                      | map_structure
                      | set_structure"""
    p[0] = p[1]


def p_list_structure(p):
    """list_structure : LSQUARE elements RSQUARE"""
    p[0] = ('list', p[2])


def p_map_structure(p):
    """map_structure : LBRACE key_value_pairs RBRACE"""
    p[0] = ('map', p[2])

def p_set_structure(p):
    """set_structure : LBRACE elements RBRACE"""
    p[0] = ('set', p[2])

def p_elements(p):
    """elements : elements COMMA value
                | value"""
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]


def p_key_value_pairs(p):
    """key_value_pairs : key_value_pairs COMMA key_value
                       | key_value"""
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]


def p_key_value(p):
    """key_value : value COLON value"""
    p[0] = (p[1], p[3])

# #Reglas para la estructuras de controlfirst': 'partridge',
#
# def p_control_structure(p):
#     """control_structure : if_structure
#                         | switch_structure"""
#
#
# ## regla if
# def p_if(p):
#     """if_structure : IF LPAREN condition RPAREN LBRACE statement RBRACE"""
#     p[0] = f"if ({p[2]})"
#
# #Regla para switch
# def p_switch(p):
#     '''switch_structure : SWITCH LPAREN expression RPAREN LBRACE cases default RBRACE'''
#     p[0] = f"switch ({p[3]}) {{\n{p[6]}\n{p[7]}\n}}"
#
#
# def p_condition(p):
#     '''condition : expression GREATER_THAN expression
#                  | expression LESS_THAN expression
#                  | expression GREATER_EQ expression
#                  | expression LESS_EQ expression
#                  | expression EQUALS expression
#                  | expression NOT_EQUALS expression'''
#     p[0] = f"{p[1]} {p[2]} {p[3]}"
#
#
# def p_cases(p):
#     '''cases : cases case
#              | case'''
#     if len(p) == 3:
#         p[0] = p[1] + '\n' + p[2]
#     else:
#         p[0] = p[1]
#
# def p_case(p):
#     '''case : CASE NUMBER COLON statement BREAK SEMICOLON'''
#     p[0] = f"case {p[2]}:\n{p[4]}\nbreak;"
#
# def p_default(p):
#     '''default : DEFAULT COLON statement
#                | empty'''
#     if len(p) == 4:
#         p[0] = f"default:\n{p[3]}"
#     else:
#         p[0] = ''
#
# def p_empty(p):
#     'empty :'
#     p[0] = ''
#
# def p_print(p):
#     '''statement : PRINT LPAREN expression RPAREN SEMICOLON'''
#     p[0] = f"print({p[3]});"
#
# def p_input(p):
#     '''statement : INPUT LPAREN expression RPAREN SEMICOLON'''
#     p[0] = f"input({p[3]});"


# Manejo de errores
def p_error(p):
    error_msg = f"Syntax error at line {p.lineno}: Unexpected token '{p.value}'\n" if p else "Syntax error in EOF\n"
    log_error(error_msg)


def log_error(error_msg):
    with open(log_filename, 'a') as log_file:
        log_file.write(f"ERROR: {error_msg}\n")


# Archivo Dart para analizar

algorithm = 'algorithms/Algoritmo2.dart'

log_filename = generate_log_filename('sintactico')

# Construcción del analizador
parser = yacc.yacc()

# Proceso de log
with open(log_filename, 'w', encoding='utf-8') as log_file:
    log_file.write(f"Syntax-analyzer started at: {datetime.datetime.now()}\n\n")

with open(algorithm, 'r') as file:
    data = file.read()

result = parser.parse(data)

with open(log_filename, 'a') as log_file:
    log_file.write(f"Parsing result:\n{result}\n")
    log_file.write(f"\nSyntax-analyzer finished at: {datetime.datetime.now()}\n\n")
