import numpy
n,m = raw_input().split(" ")
A =list(map(int,raw_input().strip().split(" "))for x in range(int(n)))
print numpy.transpose(A)
print numpy.array(A).flatten()