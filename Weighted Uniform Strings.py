#!/bin/python

import sys
ll = []
def ascii(ch):
    a=ord(ch)
    return a-96

str = raw_input().strip()
n = int(raw_input().strip())
dct =[]
dct.append(ascii(str[0]))
for i in range(len(str)):
    cnt = 2
    j = i - 1
    while str[i] == str[j]:
        dct.append(cnt * ascii(str[i]))
        cnt += 1
        j -= 1
    dct.append(ascii(str[i]))

for a0 in range(n):
    x = int(raw_input())
    if x in dct:
        ll.append("Yes")
    else:
        ll.append("No")
for i in ll:
    print i
