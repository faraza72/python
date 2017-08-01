from collections import Counter;

s = raw_input();
cnt = 0
# xaxbbbxx
final = {}

if (len(s) % 2 != 0):
    print "-1"
else:
    str1 = list(s[:len(s) / 2]);
    str2 = list(s[len(s) / 2:])
    str1Cnt = Counter(str1);
    str2Cnt = Counter(str2);

    for i in str1Cnt:
        for j in str2Cnt:
            if (i not in final and i in str2):
                final[i] = abs(str1Cnt[i] - str2Cnt[i])
            elif (i not in final and i not in str2):
                final[i] = (str1Cnt[i])

    for i in str2Cnt:
        for j in str1Cnt:
            if (i not in final and i in str1):
                final[i] = abs(str1Cnt[i] - str2Cnt[i])
            elif (i not in final and i not in str1):
                final[i] = (str2Cnt[i])

    for i in final:
        cnt += final[i]
    print cnt / 2