def is_pal(c):
    rev = str(c)[::-1]
    if int(rev) == c:
        return True

l = []
for i in range(int(raw_input())):
    N = int(raw_input())
    max_num = 0
    max_pal =[]
    for i in range(999,99,-1):

        for j in range(999,i-1,-1):

            product = i*j
            if product > N:
                continue

            if product < max_num:
                break

            if is_pal(product):
                # if product in range(0, N):
                max_num = product
                # print max_num
    l.append(max_num)


for i in l:
    print i