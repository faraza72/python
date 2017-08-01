import sys

def alternatingCharacters(s):
    temp=list(s)
    ct=0
    for i in range(1,len(temp)):
        if temp[i]==temp[i-1]:
            ct+=1
            print ct
            del temp[i]


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = alternatingCharacters(s)
    print(result)
