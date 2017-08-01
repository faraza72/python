#!/bin/python

import sys

def commonChild(s1, s2):
    length = len(s1)
    alist = []
    max=0
    for i in xrange(length):
        for j in xrange(i, length):
            alist.append(s1[i:j + 1])

    for i in alist:
        if i in s2:
            if max<len(i):
                max=len(i)
    return max


def common(s1,s2):
    l1=[]
    l2=[]
    v=0
    for i in range(len(s1)):
        print s1[i]
        print "----yahan-------"
        for j in range(v,len(s2)):
            if s1[i]==s2[j]:
                print s1[i],s2[j],v
                print "----wahan-----"
                l1.append(s1[i])
                v=j+1
    print l1
    v=0
    for i in range(len(s2)):
        for j in range(v,len(s1)):
            if s2[i]==s1[j]:
                l2.append(s2[i])
                v=j+1
    s1= ''.join(l1)
    s2= ''.join(l2)

    print s1,s2
    # max=commonChild(s1,s2)

    return max

s1 = raw_input().strip()
s2 = raw_input().strip()
result = common(s1, s2)
print(result)
