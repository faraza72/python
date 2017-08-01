#!/bin/python

import sys

def gemstones(arr):
    s=arr[0]
    ct=0
    fnlct=0
    l=[]
    for i in s:
        for j in range(1,len(arr)):
            if i in arr[j]:
                ct+=1
        if ct==len(arr)-1:
            l.append(i)

        ct=0
    return l

n = int(raw_input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
    arr_t = str(raw_input().strip())
    arr.append(arr_t)
result = gemstones(arr)
print len(set(result))
