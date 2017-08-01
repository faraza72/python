import sys
from math import sqrt

def chkprime(k):
    for i in range(2,k):
        if k % i == 0:
            return False
    return True

t = int(raw_input().strip())
for a0 in range(t):
    n = int(raw_input().strip())
    primes = [2, 3]
    t = 5
    if n > len(primes):
        while len(primes) < n:
            count = 0

            if chkprime(t):
                primes.append(t)
                count+=1
            if count==n-1:
                break
            t += 2
    print(primes[n - 1])
