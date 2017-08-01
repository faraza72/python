n,m=map(int,raw_input().split(" "))
a=map(int,raw_input().split(" "))
b=map(int,raw_input().split(" "))
ct=0
l = []
for i in xrange(max(a),min(b)+1):
    flag = 0
    for j in a:
        if i%j!=0:
            flag = 1
            break
    if(flag == 0):
        for k in (b):
            if(k%i!=0):
                flag = 1
    if flag == 0:
        ct = ct +1


print ct