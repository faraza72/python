#!/bin/python

import sys


t = int(raw_input().strip())
s=[]
for a0 in xrange(t):
    n = long(raw_input().strip())
    count=0;
    a=0;
    b=1;
    while b < n:
        sum=a+b;
        a=b;
        b=sum;
        if a % 2 == 0:
            count += a;
    s.append(count)
for i in s:
    print i


