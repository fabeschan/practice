'''
Find the rank of element with value k in an array (let's say in ascending order)
Can assume array is of distinct values
return -1 if element doesn't exist

'''
import tester

def findrank_1(a, k):
    # simplest solution but inefficient, O(n log n)
    a.sort()
    return a.index(k) if k in a else -1

def findrank_2(a, k):
    # put elements larger than k to right side, others on the left side
    # O(n), in-place

    # find k first
    if k not in a:
        return -1
    else:
        k_i = a.index(k)
        if len(a) == 1:
            return k_i

    # put k to the end of array for now
    a[-1], a[k_i] = a[k_i], a[-1]
    i, j = 0, len(a)-2
    while i <= j:
        if a[j] > k:
            j -= 1
            continue
        if a[i] < k:
            i += 1
            continue
        a[i], a[j] = a[j], a[i]

    a[i], a[-1] = a[-1], a[i]
    return i

if __name__ == '__main__':
    a = [-6, 1, 4, 7, 22, 0, 17, 51, -1, -50, 0, 13]
    k = 13

    for f in tester.list_func():
        if f.__name__.startswith('findrank'):
            b = a[:]
            print f.__name__, ':', f(b, k)
