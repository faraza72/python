#!/bin/python

import sys

def commonChild(s1, s2):
    length = len(s1)
    alist = []
    max=0
    for i in xrange(length):
        for j in xrange(i, length):
            alist.append(s1[i:j + 1])

    print alist
    for i in alist:
        if i in s2:
            print i,"----------"
            if max<len(i):
                max=len(i)
    return max


def common(s1,s2):
    l1=[]
    l2=[]

    for i in s1:
        if i in s2:
            l1.append(i)
    for i in s2:
        if i in s1:
            l2.append(i)
    s1= ''.join(l1)
    s2= ''.join(l2)
    print s1
    print s2
    max=commonChild(s1,s2)

    return max

s1 = raw_input().strip()
s2 = raw_input().strip()
result = common(s1, s2)
print(result)
