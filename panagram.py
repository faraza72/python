from collections import Counter;

str="qwertyuioplkjhgfdsazxcvbnm"
str1=raw_input()
c=0
for i in range(26):
   if str[i] in str1.lower():
       c+=1
       print str[i]
if c==26:
    print "panagaram"
else:
    print "not panagram"