from collections import deque

class Employee(object):
    def __init__(self, queue):
        self.free = True
        self.call = None
        self.queue = queue

    def handle_call(self, call):
        self.free = False
        self.call = call

    def escalate_call(self, call):
        self.end_call(call)
        call.rank += 1
        CallHandler.dispatch_call(call) # <- where to put this???

    def end_call(self, call):
        self.free = True
        self.queue.remove(self)
        self.queue.append(self)

class Fresher(Employee):
    pass

class TL(Employee):
    pass

class PM(Employee):
    pass

class Call(object):
    def __init__(self, rank):
        # rank is in range(CallHandler.LEVELS)
        self.rank = rank # minimal rank of employee who can take this call

class CallHandler(object):
    LEVELS = 3
    NUM_FRESHERS = 5

    def __init__(self):
        self.queue = []

        # fresher queue
        q = deque()
        q.extend([Fresher(q) for i in range(CallHandler.NUM_FRESHERS)])
        self.queue.append(q)

        # TL
        q = deque()
        q.extend([TL()])
        self.queue.append(q)

        # PM
        q = deque()
        q.extend([PM()])
        self.queue.append(q)

    def dispatch_call(self, call):
        for level in range(call.rank, CallHandler.LEVELS):
            q = self.queue[level]
            emp = q.pop()
            if emp.free:
                emp.handle_call(call)
                q.appendleft(emp)
                return emp
            else:
                q.append(emp)
        return None

