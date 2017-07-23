# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
d,m,y = raw_input().split(" ")
print d,m,y
print(calendar.day_name[calendar.weekday(int(y), int(m), int(d))].upper())