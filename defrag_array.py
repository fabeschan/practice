'''
Given array, put all None entries to the end, preserving the order of other entries

example:
a = [3, 2, 6, None, None, 5, None] -> [3, 2, 6, 5, None, None, None]
'''

a = [3, 2, 6, None, None, 5, None]

def defrag1(a):
    # in-place, but O(nlogn)
    a.sort(key=lambda x: 0 if x != None else 1)

def defrag2(a):
    a = [ i for i in a if i != None]

def defrag3(a):
    filter(lambda x: x != None, a)

def defrag4(a):
    count = 0
    i = 0
    while i < len(a):
        if a[i] == None:
            count += 1
            del a[i]
        else:
            i += 1
    a.extend([None]*count)

def defrag5(a):
    # doesn't work, has a few bugs
    i = 0
    j = len(a) - 1
    while i < j:
        while a[i] != None:
            i += 1
        while a[j] == None:
            j -= 1
        a[i] = a[j]
        a[j] = None

if __name__ == '__main__':
    defrag1(a)
    print a

    defrag2(a)
    print a

    defrag3(a)
    print a

    defrag4(a)
    print a

    defrag5(a)
    print a
