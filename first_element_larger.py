'''
Given an increasing sorted array A, search for smallest i such that A[i] > k (first element A[i] > k).
Return -1 if there does not exist.

For example, given A = [-1, 0, 1, 3, 6, 8] and k = 2,
return 3 because A[3] is the first element such that A[3] > 2.

'''

def foo(x, k):
    a = 0
    b = len(x)-1

    if x[b] < k:
        return -1

    while a != b:
        if x[a] > k:
            return a
        m = (a + b) / 2

        if x[m] <= k:
            a = m + 1
        else:
            b = m
    return a

'''
[3, 5m, 6a, 7b].. k=5 ;ans=2

'''

if __name__ == '__main__':
    x = [-1, 0, 1, 3, 6, 8]

    print x
    print 'k=2, ans={}'.format(foo(x, 2))
