
x = [3, 1, 5, 9, 6]
x = [1, 3, 5, 9, 6]

def bin_search(x, k, a, b):
    while x[a] != k:
        if k < x[a] or k > x[b-1]:
            return -1
        m = (a + b) / 2
        if k < x[m]:
            b = m
        else: # k >= x[m]
            a = m
        return bin_search(x, k, a, b)
    return a

def selection(x, k, a, b): # find kth smallest
    if len(x) == 0: return None
    if a == b: return x[a]

    p = a
    x[p], x[b] = x[b], x[p]
    i, j = 0, b-1
    while i < j:
        if x[i] > k and x[j] < k:
            x[i], x[j] = x[j], x[i]
        if x[i] < k:
            i+=1
        if x[j] > k:
            j-=1
    x[i], x[b] = x[i], x[b]
    if k <= i:
        return selection(x, k, a, i)
    else:
        return selection(x, k-i, i+1, b)

#print bin_search(x, 3, 0, len(x))
print selection(x, 1, 0, len(x)-1)
