# closest pair
import math
P = [[0, 0], [6, 8], [100,100] ]
n = len(P)
d = 9999999
for i in range(0, n-1):
	for j in range(i+1, n):
		d = min(d, math.sqrt( (P[i][0] -P[j][0])**2 + (P[i][1] - P[j][1])**2 ))
print(d)

