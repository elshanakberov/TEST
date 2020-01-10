a = [2, 5, 5, 5]
b = [2, 2, 3, 5, 5, 7]

ia = 0
ib = 0
output = []
while ia < len(a) and ib < len(b):
    if a[ia] < b[ib]:
        ia += 1
    elif a[ia] > b[ib]: 
        ib += 1
    else: # they are equal
        output.append(a[ia])
        ia += 1
        ib += 1

print(output)
