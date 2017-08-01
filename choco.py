#!/bin/python
import sys

def solve(n, s, d, m):
    sum=0
    count=0
    if n==1 and m==1:
        if s[0]==d:
            return 1
    else:
        for i in range(n-m):
            for j in range(i,i+m):
                sum+=s[j]
            if sum == d :
                count+=1
            sum=0

        return count


n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
