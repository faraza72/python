#!/bin/python

import sys

def theLoveLetterMystery(s):
    ct=0
    for i in range(len(s)/2):
        if s[i]!=s[len(s)-i-1]:
            ct+= abs(ord(s[i])-ord(s[len(s)-i-1]))
    return ct

li=[]
q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = theLoveLetterMystery(s)
    li.append(result)

for i in li:
    print i

