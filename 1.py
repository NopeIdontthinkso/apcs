a = input()
b = [int(x) for x in input().split()]
b.sort()
print(b)
c = []
d = []
for i in range(len(b)):
    if b[i] < 60:
        c.append(b[i])
    else:
        d.append(b[i])
if c:
    print(c[-1])
else:
    print('best case')
if d:
    print(c[0])
else:
    print('worst case')

