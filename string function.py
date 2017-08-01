def commonChild(s1):
    length = len(s1)
    alist = []
    ct=0
    maxli=[]
    for i in xrange(length):
        for j in xrange(i, length):
            alist.append(s1[i:j + 1])
    # print alist

    l=set(alist)
    print l

    for i in l:
        n = len(i)
        ct=0
        for j in range(length):
            if s[j:j + n] == i:
                ct += 1
            # print i,ct
            maxli.append(ct*n)
    return max(maxli)
s=raw_input().strip()
li = commonChild(s)
print li
