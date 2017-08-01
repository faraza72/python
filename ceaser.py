import sys

def ceaser(str,num):
    if str.islower():
        ch=ord(str)+k%26
        if ch>122:
            return chr(ch-26)
        else:
            return chr(ch)

    else:
        ch = ord(str) + k%26
        if ch > 90:
            return chr(ch - 26)
        else:
            return chr(ch)




n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

final=[]

for i in range(len(s)):
    if s[i].islower() or s[i].isupper():
        final.append(ceaser(s[i],k))
    else:
        final.append(s[i])

print ''.join(final)
