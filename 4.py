list1 = [int(x) for x in input().split()]
list2 = [int(x) for x in input().split()]
g = int(input())

a, b ,c =list1
e, d, f =list2

j = float('-inf')

for i in range(g+1):
    h = g-i
    y1 = a*i*i + b*i + c
    y2 = e*h*h + d*h + f
    k = y1 + y2
    if k > j :
        j = k 

print(j)
