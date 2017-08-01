#!/bin/python

import sys

def makingAnagrams(s1, s2):

    l1=list(s1)
    l2=list(s2)
    ct=0
    li=[]
    print len(l1),len(l2)
    for i in l1:
        if i in l2:
            li.append(i)
    return li


s1 = raw_input().strip()
s2 = raw_input().strip()
result = makingAnagrams(s1, s2)
print len(result)
final=set(result)
print final
print len(final)
