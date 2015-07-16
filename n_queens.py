class queen(object):
    def __init__(self, row, n):
        self.y = None
        self.x = row
        self.domain = range(n)

    def __repr__(self):
        return str((self.x, self.y))

def can_attack(q1, q2):
    # qi is a 2-tuple of the queen's position (x, y)
    if q1.x == q2.x or q1.y == q2.y:
        return True
    t = (q1.x - q2.x, q1.y - q2.y)
    if t[0] == t[1] or t[0] == -t[1]:
        return True
    return False

def bts(queens):
    if all(q.y != None for q in queens):
        print queens
        return True

    unassigned = None
    for q in queens:
        if q.y == None:
            unassigned = q
            break

    for d in unassigned.domain:
        unassigned.y = d
        assigned_pairs = [(q1, q2) for q1 in queens for q2 in queens if q1.y != None and q2.y != None and q1.x != q2.x]
        satisfy = True
        for q in assigned_pairs:
            if can_attack(q[0], q[1]):
                satisfy = False
                break
        if satisfy:
            bts(queens)

    unassigned.y = None # undo as we have tried all values

def bts_template(var_list):
    '''
    check if all variables are assigned
    if all_assigned:
        print assignments
        return (:return True)

    unassigned = pick unassigned variable

    for d in unassigned.domain:
        unassigned.value = d
        sat = True if constraints for all assigned variables hold else False
        if sat:
            bts(var_list) (:if bts(var_list) == True: return True)

    unassigned.value = None # undo as we have tried all values
    (:return False)
    '''

class variable:
    '''
    self.value = None # set None as the initial value
    self.domain = [...] # list of possible values

    '''

if __name__ == '__main__':
    n = 9
    queens = [queen(i, n) for i in range(n)]
    bts(queens)
