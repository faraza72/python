#!/bin/python

q = int(raw_input().strip())
for a0 in xrange(q):
    s1 = raw_input().strip()
    s2 = raw_input().strip()
    if set(s1).intersection(set(s2)):
        print 'YES'
    else:
        print 'NO'

