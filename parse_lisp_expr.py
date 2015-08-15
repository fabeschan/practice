'''
Parse these sorts of lisp-like expressions

(op, 5, 6, expr, 11)

where op is an operator and expr is another lisp expression
assume stream gives you tokens one by one, with methods hasNext() and getNext()
assume expression is valid (at least for now)

tokens:
    parentheses
    numbers
    operators
'''

