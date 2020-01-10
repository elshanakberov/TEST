import math

def quadEq(a, b, c):
	D = b**2-(4*a*c)
	if D<0:
		return "No roots"
	x1 = ((-1)*b + math.sqrt(D))/2*a
	x2 = ((-1)*b - math.sqrt(D))/2*a

	return x1, x2


print(quadEq(1, 1, -2))
