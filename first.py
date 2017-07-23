import numpy as np

l = list(map(float,raw_input().strip().split(" ")))
x = int(raw_input())
sum=0;
for i in range(len(l)):
  sum = sum + l[i]*(x**(len(l)-i-1))
print sum