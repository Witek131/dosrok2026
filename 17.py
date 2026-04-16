f = open('file\\17_28762 (1).txt').readlines()
a = [int(i) for i in f]
m = min([i for i in a if i % 23 == 0])
n = []
for x, y in zip(a, a[1:]):
    if x % m == 0 or y % m == 0:
        n.append(x + y)
print(len(n), max(n))