#!/bin/python

import sys

def funnyString(s):
    # Complete this function
    n = len(s)
    rs = s[::-1]
    for i in range(1, n):
        d1 = abs(ord(s[i]) - ord(s[i - 1]))
        d2 = abs(ord(rs[i]) - ord(rs[i - 1]))
        if d1 != d2:
            return ("Not Funny")
    else:
        return ("Funny")

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = funnyString(s)
    print(result)

