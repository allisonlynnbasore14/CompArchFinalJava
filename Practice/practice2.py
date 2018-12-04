import ply.lex as lex



# 1. Define the list of token names

# reserved lookup

reserved = {
	'if' : 'IF',
	'then' : 'THEN',
	'else' : 'ELSE',
	'while' : 'WHILE',
	'int' : 'TYPE_INT',
	'main' : 'FUNCT_MAIN',
	'for' : 'FOR'
}



tokens = ['SLT','DEFINE', 'RBRAC', 'LBRAC', 'DEFINE', 'ENDSTATEMENT', 'LPAREN','RPAREN', 'NUMBER', 'DIVIDE', 'TIMES', 'MINUS','ADD', 'STATEMENT', 'FUNCT', 'END_ARRAY', 'BEGIN_ARRAY', 'TYPE' , 'ID'] + list(reserved.values())

# 2. Define RegEx for simple tokens
# t_TYPE = r'\x69\x6E\x74' #INT
t_BEGIN_ARRAY = r'\x5B'
t_END_ARRAY = r'\x5d'	
t_DEFINE  = r'\x3D'
t_ADD = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_RBRAC = r'\x7D'			# {
t_LBRAC = r'\x7B'			# }
t_ENDSTATEMENT = r'\x3B'	#;
t_SLT = r'\x3C'				# <



# 3. Regex rule with action code
def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t 

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type = reserved.get(t.value,'ID')	#check for reserved words
	return t

# 4. Track line numbers

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# 5. String containing ignored characters (spaces and tabs)
t_ignore = ' \t, \n, \r'

# Build the lexer
lexer = lex.lex()

# 6. Error handling rule
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)


# Test it out
data = '''
int main()
{
    
    int sum = 0;
    
    int i = 0;
    
    for(i;i<11;i++){
        
        sum = sum + i;
    }

    return 0;
}
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