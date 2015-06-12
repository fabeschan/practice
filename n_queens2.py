
class queen(object):
    def __init__(self, i, n):
        self.row = i
        self.value = None
        self.domain = range(n)

    def __repr__(self):
        return str((self.row, self.value))

def check_constraint(q1, q2):
    # return False if q1 and q2 can attack each other
    if q1.row == q2.row or q1.value == q2.value:
        return False
    t = (q1.row - q2.row, q1.value - q2.value)
    if t[0] == t[1] or t[0] == t[-1]:
        return False
    return True

def bts(queens):
    # if all vars assigned, print and return True
    if all(q.value != None for q in queens):
        print queens
        return True

    # pick unassigned
    for q in queens:
        if q.value == None:
            u = q
            break

    for d in u.domain:
        u.value = d
        assigned = [q for q in queens if q.value != None]
        pairs = [(q1, q2) for q1 in queens for q2 in queens if q1.row != q2.row and q1.value != None and q2.value != None]
        # sat = check constraints
        sat = all(check_constraint(*q) for q in pairs)
        if sat:
            if bts(queens):
                return True

    u.value = None
    return False

if __name__ == '__main__':
    n = 4
    queens = [queen(i, n) for i in range(0, n)]
    bts(queens)
