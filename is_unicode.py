'''
Verify that a list of bytes is in unicode format

1: 0xxxxxxx
2: 110xxxxx 10xxxxxx
3: 1110xxxx 10xxxxxx 10xxxxxx
4: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
5: 111110xx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx
6: 1111110x 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx
7: 11111110 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx
8: 11111111 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx

UNTESTED
'''

def num_leading_ones(n):
    count = 0
    while n & 0b10000000 != 0:
        count += 1
        n <<= 1
    return count

def is_unicode(c):
    if len(c) == 1:
        return c[0] & 0b10000000 == 0
    else:
        if len(c) != num_leading_ones(c[0]):
            return False
        for b in c[1:]:
            if 0b11000000 & b != 0b10000000:
                return False
        return True
