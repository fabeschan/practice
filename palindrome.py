# find length of longest palindrome

def manacher(s):
    expanded = "#" + '#'.join(s) + "#"
    array = [0] * len(expanded)
    R = 0
    C = 0
    for i in range(len(expanded)):
        # crange = R<-C->R
        # if i in crange and (i+array[2*c - i]) <= C+R:
        #   array[i] = array[2*c - i] (at least this much)
        #
        # take array[i] and expand/compare ends

def centers(s):
    # centered at whole number index
    max_count = 1
    for i in range(len(s)):
        count = 1
        j, k = i+1, i-1
        while 1:
            if 0 <= j < len(s) and 0 <= k < len(s) and s[j] == s[k]:
                count += 2
                j += 1
                k -= 1
            else:
                max_count = max(max_count, count)
                print ">>{}>>{}".format(i, count)
                break

    for i in range(len(s)):
        count = 0
        j, k = i+1, i
        while 1:
            if 0 <= j < len(s) and 0 <= k < len(s) and s[j] == s[k]:
                count += 2
                j += 1
                k -= 1
            else:
                max_count = max(max_count, count)
                print ">>{}>>{}".format(i+0.5, count)
                break
    return max_count

if __name__ == '__main__':
    s = 'abacabac'
    print centers(s)
    print manacher(s)

    s = 'aabbcdd'
    print centers(s)
