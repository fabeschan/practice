def bts(var_list):
    if all_assigned():
        print assignments # or add to results
        return True

    u = pick_unassigned_var()

    for d in u.domain:
        u.value = d
        sat = constraints_hold_for_all_assigned_vars()
        if sat and bts(var_list):
                return True

    u.value = None # undo as we have tried all values
    return False

class variable:
    def __init__(self, domain)
    self.value = None # set None as the initial value
    self.domain = domain # list of possible values

'''
def bts(var_list):
    if all_vars_assigned():
        print assignments
        return True

    u = pick_unassigned_var()
    for d in u.domain:
        u.value = d
        sat = contraints_hold_for_all_assigned_vars()
        if sat and bts(var_list):
            return True

    u.value = None
    return False
'''
