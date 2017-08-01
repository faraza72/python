#!/bin/python

import sys


def gcd(x,y):
    while y != 0:
        x,y = y,x % y
    return x


# define lcm function
def findlcm(x, y):

   lcm = (x*y)//gcd(x,y)
   return lcm


t = int(raw_input().strip())
lcm = 1
l =[]
for a0 in xrange(t):
    n = int(raw_input().strip())
    for i in range(2,n+1):
        lcm = findlcm(lcm,i)
    l.append(lcm)
for i in l:
    print i