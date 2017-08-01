import sys

a= raw_input().strip()
b = raw_input().strip()
n = len(a) + 1
m = len(b) + 1

lcs = [[0] * (n) for i in range(m)]  # lcs[i][j] holds the length of the LCS between a[:i] and b[:j]


maximumLength = 0
for i in range(1, n):
    for j in range(1, m):
        if (a[i - 1] == b[j - 1]):
            print a[i-1],b[j-1],'======'
            lcs[i][j] = lcs[i - 1][j - 1] + 1
            print lcs,"------"
        else:
            lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])
            print lcs[i][j - 1], lcs[i - 1][j],'#######'

        maximumLength = max(maximumLength, lcs[i][j])

print (maximumLength)