'''
Determine if an integer n is a power of 2, without using arithmetic operators

'''


def is_pow2(n):
    if n <= 0:
        return False

    # if is power of 2, binary representation has exactly one 1
    # example: 0000100, 0001000, 001
    while n:
        if n == 1:
            return True
        if 1 & n:
            return False
        n >>= 1
    return False

if __name__ == '__main__':
    n = 9
    print n, ':', is_pow2(n)

    n = -4
    print n, ':', is_pow2(n)

    n = 4
    print n, ':', is_pow2(n)

    n = 99
    print n, ':', is_pow2(n)

    n = 128
    print n, ':', is_pow2(n)
