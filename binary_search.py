from IPython import embed

def binary_search_recursive(x, k, a=0, b=-1):
    if b == -1:
        b = len(x)

    if x[a] == k and x[a] <= k and k <= x[b-1]:
        return a
    m = (a + b) / 2
    if k < x[m]:
        return binary_search_recursive(x, k, a, m)
    else:
        return binary_search_recursive(x, k, m, b)

def binary_search_iterative(x, k):
    a = 0
    b = len(x)

    while x[a] != k and x[a] <= k and k <= x[b-1]:
        m = (a + b) / 2
        if k < x[m]:
            b = m
        else:
            a = m
    return a

if __name__ == '__main__':
    x = [52, 35, 123, 74, 77, 0, 3, -1, 15, 22, 10, 200, 260, 90, -8, -808]
    x.sort()

    print x
    for k in x:
        print 'i[{}]? {}: {}'.format(k, x.index(k), binary_search_iterative(x, k))
    for k in x:
        print 'r[{}]? {}: {}'.format(k, x.index(k), binary_search_recursive(x, k))

    embed()
