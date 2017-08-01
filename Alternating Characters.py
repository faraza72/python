import sys

def alternatingCharacters(s):
    ct=0
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            ct+=1
    return  ct


q = int(raw_input().strip())
li=[]
for a0 in xrange(q):
    s = raw_input().strip()
    result = alternatingCharacters(s)
    li.append(result)

for i in li:
    print i

