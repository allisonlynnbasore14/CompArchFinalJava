import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lexer import tokens

def p_expression(self, p):
    """ expression  : assignment_expression
                    | expression COMMA assignment_expression
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        if not isinstance(p[1], c_ast.ExprList):
            p[1] = c_ast.ExprList([p[1]], p[1].coord)

        p[1].exprs.append(p[3])
        p[0] = p[1]

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_assignment_expression(self, p):
    """ assignment_expression   : conditional_expression
                                | unary_expression assignment_operator assignment_expression
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ast.Assignment(p[2], p[1], p[3])

def p_jump_statement_4(self, p):
    """ jump_statement  : RETURN expression SEMI
                        | RETURN SEMI
    """
    p[0] = ast.Return(p[2] if len(p) == 4 else None)

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
