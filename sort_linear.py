
def radix_sort(s):
    # s: a list of integers
    if not s:
        return s

    max_ = s[0]
    for i in s:
        max_ = max(max_, i)

    exp = 0
    while max_:
        # put into buckets starting from the least significant digit
        buckets = []
        for i in range(10):
            buckets.append([])

        for i in s:
            buckets[i % (10**(exp+1)) / 10**exp].append(i)

        s = []
        for b in buckets:
            s.extend(b)

        max_ /= 10
        exp += 1

    # final bucket: positive and negative
    ss = []
    for i in s[::-1]:
        if i < 0:
            ss.append(i)
        else:
            break

    for i in s:
        if i >= 0:
            ss.append(i)
        else:
            break
    return ss

def radix_sort_string(s):
    # assume ascii, so a bucket of size 256
    if not s:
        return s

    max_ = len(s)

    exp = 0
    while max_:
        # put into buckets starting from the least significant digit
        buckets = []
        for i in range(256):
            buckets.append('')

        for i in s:
            buckets[ord(i) % (256**(exp+1)) / 256**exp] += i

        s = ''
        for b in buckets:
            s += b

        max_ /= 10
        exp += 1
    return s

def radix_sort_string_list(s):
    # s: a list of strings
    pass

if __name__ == '__main__':
    s = [45, 660, 19, 4, -79, 0, -1, -2, 152, -6, -5, -17, -13, -10, -11, 6783, 1099, 667, -555]
    print radix_sort(s)

    s = "afhoegijlsgiikf"
    print radix_sort_string(s)
