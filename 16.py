import numpy
n,m = raw_input().split(" ")
A =list(map(int,raw_input().strip().split(" "))for x in range(int(n)))
arr = numpy.array(A)
print numpy.mean(A,axis=1)
print numpy.var(A,axis=0)
print numpy.std(A,axis=None)