#!/bin/python

import sys
import numpy


n = int(raw_input().strip())
unsorted = []
unsorted_i = 0
final=[]
for unsorted_i in xrange(n):
    unsorted_t = str(raw_input().strip())
    unsorted.append(unsorted_t)
max= numpy.Array(unsorted)

print sorted(max)
# for i in range(n):
#     for j in range(n-i-1):
#         if long(unsorted[j])>long(unsorted[j+1]):
#             t=unsorted[j]
#             unsorted[j]=unsorted[j+1]
#             unsorted[j+1]=t
#
# for i in unsorted:
#     print i