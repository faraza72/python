import numpy
n,m = raw_input().split(" ")
A = list(map(int,raw_input().strip().split(" "))for x in range(int(n)))
print numpy.product(numpy.sum(A,axis=0))
