A = [5, 1, 7, 4, 2, 3, 6]
n = len(A)
for i in range(0, n-2):
	mini = i
	for j in range(i+1, n-1):
		if A[j]<A[mini]:
			mini = j
	A[i], A[mini] = A[mini], A[i]

print(A)
