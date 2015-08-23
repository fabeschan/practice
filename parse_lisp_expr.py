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

# solution #1: make a tree then traverse the tree

class Node:
    def __init__(self):
        # if children is empty, data is a number
        # else, data is an op
        self.data = None
        self.children = []
    def __repr__(self):
        return '<{}> {}'.format(self.data, self.children)

class Stream:
    def __init__(self, s=[]):
        self.items = s

    def hasNext(self):
        return len(self.items) > 0

    def getNext(self):
        if self.hasNext():
            t = self.items[0]
            self.items = self.items[1:]
            return t
        else:
            return None

def parse_expr(s):
    root = None
    stack = []

    while s.hasNext():
        c = s.getNext()
        if c == '(':
            n = Node()
            n.data = s.getNext() # set op
            if stack:
                stack[-1].children.append(n)
            stack.append(n)
            if root is None:
                root = n
        elif c == ')':
            stack.pop()
        else:
            n = Node()
            n.data = c # set numbers
            stack[-1].children.append(n)
        print stack
    return root

if __name__ == '__main__':
    s = ['(', 'mult', '(', 'mult', 5, 6, ')', 5, 6, ')']
    stream = Stream(s)
    parse_expr(stream)

