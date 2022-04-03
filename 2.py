a = [int(x) for x in input()]
b = 0
c = 0
for i in range(len(a)):
    if (i+1)%2==0:
        b += a[i]
    else:
        c += a[i]
print(abs(c-b))
