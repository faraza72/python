#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,o= raw_input().strip().split(' ')
a,o = [int(a),int(o)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))
appleCount=0
orangeCount=0
for i in apple:
    if a+i>=s and a+i<=t:
        appleCount+=1
for i in orange:
    if o+i>=s and o+i<=t:
        orangeCount+=1
print appleCount
print orangeCount