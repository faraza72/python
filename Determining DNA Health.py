

def find_all(a_str,sub):
    v = len(sub)
    cnt = 0;
    for i in range(0,len(a_str)-v+1):
        if(a_str[i:i+v] == sub):
            cnt +=1
    return cnt

def check(l1,l2,first,last,h):
    s= 0
    for i in range(first,last+1):
        s+=find_all(l2,l1[i])*h[i]
    return s
   
n = int(raw_input().strip())
genes = raw_input().strip().split(' ')
health = map(int, raw_input().strip().split(' '))
s = int(raw_input().strip())
ll =[]
for a0 in range(s):
    first,last,d = raw_input().strip().split(' ')
    ll.append(check(genes,d,int(first),int(last),health))
print min(ll),max(ll)