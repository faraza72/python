#!/bin/python

import sys

def anagram(s):
    n = len(s)
    if n%2!=0:
        return -1
    else:
        a=s[:n/2]
        b=s[n/2:]
        print "\nlen(set(a)): ",len(set(a))
        print "len(set(b): ",len(set(b))


        return 0

q = int(raw_input().strip())
result=[]
for a0 in xrange(q):
    s = raw_input().strip()
    result.append(anagram(s))
for i in range(q):
    print result[i]

