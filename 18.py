s = raw_input()
l = len(s)
finalstr = ''
for i in range(l-1):
    print i, s[i]
    if(s[i] == s[i+1]):
        i += 2
        print "jump",i
    else:
        finalstr += s[i]
print finalstr
