m = int(raw_input())
A = set(map(int,raw_input().strip().split(" ")))
n = int(raw_input())
B = set(map(int,raw_input().strip().split(" ")))
a=[A-B]
b=[B-A]
a=list(a) + list(b)
print sorted(a)
#for i in range(int(len(a))):
  #  print a[i]