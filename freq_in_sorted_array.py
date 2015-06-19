import random as rd
elements = [3, 52, 47, 17, 841, 586, 774, 0]

def construct_array():
    a = []
    for e in elements:
        a.extend([e for i in range(rd.choice(range(10)))])
    a.sort()
    return a

def count_elements(a):
    f = {}
    for e in a:
        freq = f.get(e, 0)
        freq += 1
        f[e] = freq

    return [(k, v) for k, v in f.items()]

a = construct_array()
print a
print count_elements(a)

def count_elements_better(a):
    f = {}
    cur = 0
    start = 0
    end = len(a) - 1

    while start <= end:
        while cur < end:
            # find rightmost index where a[index] = a[start]
            mid = (cur + end) / 2
            if a[cur] == a[mid]:
                # try again on the right
                cur = mid + 1
            else:
                # try on the left
                end = mid - 1
        count = cur - start + 1
        f[a[start]] = count
        start = cur + 1
        end = len(a) - 1
        cur = start

    return [(k, v) for k, v in f.items()]

print count_elements_better(a)
