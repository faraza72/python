s = raw_input()
s2 = ''
for i in range(len(s)/3):
  s2 += 'SOS';
cnt = 0
for i in range(len(s)):
  if(s[i]!=s2[i]):
	cnt += 1
print cnt