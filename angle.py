# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = int(raw_input())
bc = int(raw_input())
mc = math.sqrt(math.pow(ab,2)+math.pow(bc,2))/2
mb =  math.sqrt(math.pow(bc,2)-math.pow(mc,2))
angle = math.acos(mc/bc)
dg = int(round(math.degrees(angle)))
print str(dg+"°")
