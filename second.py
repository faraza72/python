import numpy
def arr_input(N=6):
    print 'Enter %d by %d array, one row per line (elements separated by blanks)' % (N, N)    
    return [[n if abs(n)<=9 else 0 for n in map(int, raw_input().split())] for i in range(N)]
print 'Enter the dimension'
n=raw_input()
A = arr_input(int(n))
print A
print numpy.linalg.det(A)