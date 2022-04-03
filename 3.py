list1 = [int(x) for x in input().split()]
list1.sort()
a, b, c = list1
print(*list1)
if c >= a + b :
    print('No')
else:
    if a**2 + b**2 == c^2:
        print('Right')
    if a**2 + b**2 < c^2:
        print('Obtuse')
    if a**2 + b**2 > c^2:
        print('Acute')
