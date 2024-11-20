import ply.lex as lex

tokens = (
    'number'
    'id',  # Identificadores
    'begin',
    'end',
    'const',
    'const_assign',      # =
    'semicolon',   # ;
    'type',
    'var',
    'comma',       # ,
    'colon',       # :
    'integer',
    'real',
    'char',
    'boolean',
    'array',
    'lbracket',    # [
    'rbracket',    # ]
    'of',
    'record',
    'function',
    'procedure',
    'lparen',      # (
    'rparen',      # )
    'while',
    'do',
    'if',
    'then',
    'for',
    'write',
    'read',
    'assignment',  # :=
    'to',
    'else',
    'false',
    'true',
    'and',
    'or',
    'greater',     # >
    'less',        # <
    'equal',       # ==
    'notequal',    # !=
    'GoE',         # >=
    'LoE',         # <=
    'sum',         # +
    'sub',         # -
    'mult',        # *
    'div',         # /
    'dot'          # .
)

# Expressões regulares para os tokens

t_begin         = r'begin'
t_end           = r'end'
t_const         = r'const'
t_const_assign  = r'='
t_semicolon     = r';'
t_type          = r'type'
t_var           = r'var'
t_comma         = r','
t_colon         = r':'
t_integer       = r'integer'
t_real          = r'real'
t_char          = r'char'
t_boolean       = r'boolean'
t_array         = r'array'
t_lbracket      = r'\['
t_rbracket      = r'\]'
t_of            = r'of'
t_record        = r'record'
t_function      = r'function'
t_procedure     = r'procedure'
t_lparen        = r'\('
t_rparen        = r'\)'
t_while         = r'while'
t_do            = r'do'
t_if            = r'if'
t_then          = r'then'
t_for           = r'for'
t_write         = r'write'
t_read          = r'read'
t_assignment    = r':='
t_to            = r'to'
t_else          = r'else'
t_false         = r'false'
t_true          = r'true'
t_and           = r'and'
t_or            = r'or'
t_greater       = r'>'
t_less          = r'<'
t_equal         = r'=='
t_notequal      = r'!='
t_GoE           = r'>='
t_LoE           = r'<='
t_sum           = r'\+'
t_sub           = r'-'
t_mult          = r'\*'
t_div           = r'/'
t_dot           = r'\.'

def t_float(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_id(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in tokens:  # Se o identificador for uma palavra-chave
        t.type = t.value   # Muda o tipo para a palavra-chave correspondente
    return t

def t_number(t):
    r'\d+'
    t.value = int(t.value)    
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere desconhecido  {t.value[0]} na linha {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
lexer.lineno = 1

inFile = open('exemplo1.sp','r')
outFile = open('saida.txt','w')
data = inFile.read()
lexer.input(data)
tokens = []

for tok in lexer:
    tokens.append(tok)
    tokenStr = str(tok)
    outFile.write(tokenStr + '\n')

inFile.close()
outFile.close()

for token in tokens:
    print(token)
