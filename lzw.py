
alphabet = '01'

def compress(s):
    output = ''

    # init dict
    d = {}
    i = 0
    for c in alphabet:
        d[c] = i
        i += 1

    w = ''
    for c in s:
        if (w + c) in d:
            w += c
        else:
            output += str(d[w]) if w else ''
            d[w+c] = i
            i += 1
            w = ''
    return output

def decompress(s):
    output = ''

    # init dict
    d = {}
    d2 = set()
    i = 0
    for c in alphabet:
        d[str(i)] = c
        d2.add(c)
        i += 1

    w = ''
    for c in s:
        if (w+d[c][0]) not in d2:
            d[str(i)] = w+d[c][0]
            d2.add(w+d[c][0])
            i += 1
        output += d[c]
        w = d[c]
    return output

if __name__ == '__main__':
    s = "101011101010111011101010001011"
    print "compressed:", compress(s)
    print "decompressed:", decompress(s)
    print "correct?", decompress(s) == s
