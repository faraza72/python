
import sys

def minSteps(n, B):
    # Complete this function
    ct=0
    s=list(B)
    for i in range (n-2):
        if s[i]=='0' and s[i+1]=='1' and s[i+2]=='0':
            ct+=1
            s[i+2]='1'
    return  ct
n = int(raw_input().strip())
B = raw_input().strip()
result = minSteps(n, B)
print(result)