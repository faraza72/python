#!/bin/python

import sys

from collections import Counter

def isValid(S):

    char_map = Counter(S)
    print char_map
    char = Counter(char_map.values())
    print char
    if len(char) == 1:
        return "YES"
    if len(char) == 2:
        for v in char.values():
            print v
            if v == 1:
                return "YES"
    return "NO"

s = raw_input().strip()
result = isValid(s)
print(result)
