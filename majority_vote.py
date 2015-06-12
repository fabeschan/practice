

a, b, c, d, e, f = 0, 1, 2, 3, 4, 5

ex1 = [a, a, b, a, c]
ex2 = [a, b, b, a, b, b, b, b, e, e, f, e, b]

def majority(s):
    if not s:
        return
    elif len(s) == 1:
        return s[0]

    elem = s[0]
    count = 1

    for i in range(1, len(s)):
        if elem == s[i]:
            count += 1
        elif count:
            count -= 1
        else:
            elem = s[i]
            count = 1

    #check
    count = 0
    for e in s:
        if e == elem:
            count += 1

    if count > len(s) / 2:
        return elem
    else:
        return None

def half_or_more(s):


if __name__ == '__main__':
    for ex in [ex1, ex2]:
        print majority(ex)
