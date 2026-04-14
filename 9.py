f = open('file\\9_28755 (1).txt').readlines()
k = 0
for i in f:
    a = [int(j) for j in i.split()]
    print(a)
    if max(a) < sum(a) - max(a) and a[0] + a[1] != a[2] + a[3] and a[0] + a[2] != a[1] + a[3] and a[0] + a[3] != a[1] + \
            a[2]:
        k += 1
print(k)
