import ply.lex as lex



# 1. Define the list of token names

tokens = (
	'NUMBER',
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE',
	'LPAREN',
	'RPAREN',
	)


# 2. Define RegEx for simple tokens

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# 3. Regex rule with action code

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t 

# 4. Track line numbers

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# 5. String containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Build the lexer
lexer = lex.lex()

# 6. Error handling rule
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)


# Test it out
data = '''
3 + 4 * 10
+ -20 *2
'''
 
# Give the lexer some input
lexer.input(data)
 
# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)

# output will be 
# type, value, lineno, lexpos