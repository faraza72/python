#!/bin/python

import sys

def richieRich(s, n, k):
    li=list(s)
    for i in range(n/2):
        if li[i]!=li[n-i-1]:
            if li[i]=='9':
                li[n-i-1]='9'
                k-=1
            elif li[n-i-1]=='9':
                li[i] = '9'
                k-=1
            elif li[i]!=li[n-i-1]!='9':
                li[i]=li[n-i-1]='9'
                k-=2
        # print k
        # print "--------------------"
        if k>0 and li[i] == li[n - i - 1]:
            if li[i] == li[n - i - 1] != '9':
                li[i] = li[n - i - 1] = '9'
                k -= 2
    # print k
    if k<0:
        return -1
    else:
        return ''.join(li)



n,k = raw_input().strip().split(' ')
n=int(n)
k=int(k)
s = raw_input().strip()
result = richieRich(s, n, k)
print(result)