def average(array):
    a= set(array)
    b=float(sum(a)/len(a))
    return b
n= int(raw_input())
arr = map(int, raw_input().split())
result = average(arr)
print result