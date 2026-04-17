f = open('file\\24_28765.txt').read()
l = 0
n = 0
m = []
for i in range(1, len(f)):
    if f[i - 1] + f[i] == 'BC':
        n += 1
    while n > 180 and l < len(f):
        if f[l - 1] + f [l] == 'BC':
            n -= 1
        l += 1

    if n <= 180:
        m.append(i - l + 2)
print(max(m))
