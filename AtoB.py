s = 'ABBB'
n = len(s)
c = 0
for i in range(n-1):
	for j in range(i+1, n):
		if s[i] == 'A' and s[j] == 'B':
			c += 1
print(c) 
