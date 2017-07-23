#!/bin/python

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    flag=0
    if x1<x2 and v1>v2:
        while 1:
            x1+=v1
            x2+=v2
            if x1==x2:
                flag=1
                break
    else:
        if x1>x2 and v1<v2:
            while 1:
                x1+=v1
                x2+=v2
                if x1==x2:
                    flag=1
                    break
    if flag==0:
        return 'NO'
    else:
        return 'YES'

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
