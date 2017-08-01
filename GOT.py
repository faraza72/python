#!/bin/python

import sys

def isPalin(s):
    for i in range(len(s)/2):
        if s[i]==s[len(s)-i]:
            return True
        else:
            return False
        

def gameOfThrones(s):

s = raw_input().strip()

result = gameOfThrones(s)

print(result)
