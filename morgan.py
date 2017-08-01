# import sys
#
# t = int(raw_input())
#
# st=[]
# for a in range(t):
#     x = raw_input().strip()
#     y = raw_input().strip()
#     x_cnt=0
#     y_cnt=0
#     final = []
#     while x_cnt<len(x) and y_cnt<len(y):
#         if x[x_cnt]<y[y_cnt]:
#             final.append(x[x_cnt])
#             x_cnt+=1
#         else:
#             final.append(y[y_cnt])
#             y_cnt+=1
#     while x_cnt<len(x):
#         final.append(x[x_cnt])
#         x_cnt+=1
#     while y_cnt<len(y):
#         final.append(y[y_cnt])
#         y_cnt+=1
#     st.append(''.join(final))
#
# for i in st:
#     print i
# ====================2nd program=====================
import sys

t = int(raw_input())

st=[]
for a in range(t):
    x = raw_input().strip()
    y = raw_input().strip()
    x_cnt=0
    y_cnt=0
    print len(x),len(y)
    final = []
    while x_cnt<len(x) and y_cnt<len(y):
        if x[x_cnt] < y[y_cnt]:
            final.append(x[x_cnt])
            x_cnt+=1
        elif x[x_cnt] > y[y_cnt]:
            final.append(y[y_cnt])
            y_cnt+=1
        elif x[x_cnt]==y[y_cnt]:
            print x_cnt,y_cnt
            if x[x_cnt+1] <= y[y_cnt+1]:
                final.append(x[x_cnt])
                x_cnt+=1
            else:
                final.append(y[y_cnt])
                y_cnt += 1
    while x_cnt<len(x):
        final.append(x[x_cnt])
        x_cnt += 1
    while y_cnt<len(y):
        final.append(y[y_cnt])
        y_cnt += 1
    st.append(''.join(final))

    print x_cnt,y_cnt

for i in st:
    print i
