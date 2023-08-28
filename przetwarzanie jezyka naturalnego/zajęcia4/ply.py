from ply import lex
from ply import yacc


# list of token names. This is always required
tokens = (
    'NUMBER',
    'OPERATE',
    'SIZE',
    'KIND',
    'COLOR',
    'MATERIAL',
    'HOW',
    'MANY'
)


# main parser rule(command)
def p_command(p):
    'command : OPERATE NUMBER article'
    index = p[3]
    # buy article
    if p[1] == 'Buy':
        tab[index] += p[2]
        print(f'OK. I am buying {str(p[2])} new articles indexed as {str(index)}.')
        print(f'No of articles in shop: {str(tab[index])}')
    # sell article
    elif p[1] == 'Sell':
        if p[2] > tab[index]:
            print('I do not have as many articles as you want')
        else:
            tab[index] -= p[2]
            print(f'OK. I am selling {str(p[2])} articles indexed as {str(index)}.')
            print(f'No of articles in shop: {str(tab[index])}')


def p_command_howmany(p):
    'command : HOW MANY article'
    print(f'You have {tab[p[3]]}')


def t_HOW(t):
    r'How'
    return t


def t_MANY(t):
    r'many'
    return t


# rules may include actions
def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


def t_OPERATE(t):
    r'Buy | Sell'
    return t


def t_SIZE(t):
    r'tiny | small | big | large'
    if t.value == 'tiny':
        t.value = 1
    elif t.value == 'small':
        t.value = 2
    elif t.value == 'big':
        t.value = 3
    elif t.value == 'large':
        t.value = 4
    return t


def t_KIND(t):
    r'box(es)? | ring(s)?'
    if t.value == 'box' or t.value == 'boxes':
        t.value = 1
    else:
        t.value = 2
    return t


def t_MATERIAL(t):
    r'metal | plastic'
    if t.value == 'metal':
        t.value = 1
    elif t.value == 'plastic':
        t.value = 2
    return t


def t_COLOR(t):
    r'black | white | red | green | blue'
    if t.value == 'black':
        t.value = 1
    elif t.value == 'white':
        t.value = 2
    elif t.value == 'red':
        t.value = 3
    elif t.value == 'green':
        t.value = 4
    elif t.value == 'blue':
        t.value = 5
    return t


# error handling rule(to deal with words out of vocabulary)
def t_error(t):
    print(f'Illegal character {t.value[0]}')
    t.lexer.skip(1)


# a string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


def p_attribute_color(p):
    'attribute : COLOR'
    p[0] = p[1]


def p_attribute_material(p):
    'attribute : MATERIAL'
    p[0] = p[1] * 10


def p_attribute_size(p):
    'attribute : SIZE'
    p[0] = p[1] * 100


def p_attribute_kind(p):
    'attribute : KIND'
    p[0] = p[1] * 1000


def p_article_attribute(p):
    "article : attribute attribute attribute attribute"
    p[0] = p[1] + p[2] + p[3] + p[4]


# error rule for syntax error
def p_error(p):
    print('Syntax error in input')


# MAIN PROGRAM
# initialize table of articles (zero articles at the beginning)
tab = []
for index in range(3000):
    tab.append(0)

# building the lexer
lexer = lex.lex()

# build the parser
parser = yacc.yacc()

# main loop
while True:
    s = input('What can i do for you? \n')
    if s == 'Bye':
        break
    parser.parse(s)

