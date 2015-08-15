'''
Given array, put all None entries to the end, preserving the order of other entries

example:
a = [3, 2, 6, None, None, 5, None] -> [3, 2, 6, 5, None, None, None]
'''

import tester

a = [None, 3, 2, 6, None, None, 5, None]

def defrag_1(a):
    # in-place, but O(nlogn)
    a.sort(key=lambda x: 0 if x != None else 1)

def defrag_2(a):
    # O(n), but not in-place
    b = [ i for i in a if i != None]
    a[0:len(b)] = b
    a[len(b):len(a)] = [None]*(len(a)-len(b))

def defrag_3(a):
    i, j = 0, 0
    while i < len(a):
        if a[i] is None and a[j] is not None:
            j = i
            i += 1
        elif a[i] is None and a[j] is None:
            i += 1
        elif a[i] is not None and a[j] is not None:
            i += 1
        elif a[i] is not None and a[j] is None:
            a[j] = a[i]
            a[i] = None
            i = j

def defrag_4(a):
    # in-place, but O(n^2)
    count = 0
    i = 0
    while i < len(a):
        if a[i] == None:
            count += 1
            del a[i]
        else:
            i += 1
    a.extend([None]*count)

if __name__ == '__main__':
    for f in tester.list_func():
        if f.__name__.startswith('defrag'):
            b = a[:]
            f(b)
            print f.__name__, ':', b
