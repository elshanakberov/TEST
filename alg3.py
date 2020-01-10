import math
P = [[0,0], [3,4], [10,10], [15,15], [116,116]]
Q = [[0,0], [3,4], [10,10], [15,15], [116,116]]

def brute(P):
	n = len(P)
	d = math.inf
	for i in range(0, n-1):
		for j in range(i+1, n):
			d = min(d, math.sqrt((P[i][0]-P[j][0])**2 +(P[i][1]-P[j][1])**2 ))
	return d
def alg3(P, Q):
	n = len(P)
	if n<= 3:
		# brute force
		return brute(P)			
	else:
		half = (n+1)//2
		Pl = P[:half]
		Ql = Q[:half]
		Pr = P[half:]
		Qr = Q[half:]
		dl = alg3(Pl, Ql)
		dr = alg3(Pr, Qr)
		d = min(dl, dr)
		m = P[half-1][0]
		S = [a for a in Q if abs(a[0]-m) < d]
		dminsq = d**2
		num = len(S)
		for i in range(num-1):
			k = i+1
			while k<num-1 and (S[k][1] - S[i][1])**2 < dminsq:
				dminsq = min((S[k][0] - S[i][0])**2 + (S[k][1] - S[i][1]), dminsq)
				k += 1
	return math.sqrt(dminsq)	

print(alg3(P, Q))
