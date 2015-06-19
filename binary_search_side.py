
def binary_search_left(x, k):
    a = 0
    b = len(x)-1
    while a != b:
        if k < x[a] and x[b] < k:
            return a
        m = (a + b) / 2
        if x[m] < k:
            a = m + 1
        else:
            b = m
    return a

def binary_search_right(x, k):
    a = 0
    b = len(x)
    while a != b:
        if k < x[a] and x[b] < k:
            return b
        m = (a + b) / 2
        if x[m] <= k:
            a = m + 1
        else:
            b = m
    return b

'''
[2am, 3b]
[3m, 3ab]


'''

if __name__ == "__main__":
    x = [2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7]

    print x
    print "left"
    for a in list(set(x)):
        print "[{}]: {}? - {}".format(a, binary_search_left(x, a), x.index(a))
    print
    print "right"
    for a in list(set(x)):
        print "[{}]: {}? - {}".format(a, binary_search_right(x, a), len(x) - 1 - x[::-1].index(a))
