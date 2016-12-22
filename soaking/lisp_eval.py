'''
lisp expressions:

expr =
    (expr,expr,op) |
    int

'''


def is_int(s):
    try:
        int(s)
    except:
        return False
    return True

def perform_op(op, n1, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2


# use recursion probably
# assume valid inputs

def lisp_eval(expr):
    if is_int(expr):
        return int(expr)

    # extract expr1, expr2 and op
    # recursively evaluate

    expr1, expr2, op = '', '', ''
    counter = 0

    i = 1
    while 1:
        c = expr[i]
        if c == '(':
            counter += 1
        elif c == ')':
            counter -= 1

        if c == ',' and counter == 0:
            i += 1
            break
        expr1 += c
        i += 1

    while 1:
        c = expr[i]
        if c == '(':
            counter += 1
        elif c == ')':
            counter -= 1

        if c == ',' and counter == 0:
            i += 1
            break
        expr2 += c
        i += 1

    while 1:
        c = expr[i]
        if c == ')':
            break
        op += c
        i += 1

    val1 = lisp_eval(expr1)
    val2 = lisp_eval(expr2)
    return perform_op(op, val1, val2)

s = '(1,2,+)'
ss = '(%s,%s,+)' % (s, s)
sss = '(%s,%s,-)' % (ss, '(44,5,-)')

print lisp_eval(sss)
