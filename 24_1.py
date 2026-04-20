f = open('24_1040.txt').read()
k = 0
l = 0
m = 0
for l in range(len(f)):
    for r in range(l + 1, len(f)):
        c = f[l: r + 1]
        d = 0
        for i in range(ord('a'), ord('z') + 1):
            if chr(i) in c:
                d = 1
                break
        if d == 0:
            m = max(m, len(c))
        else:
            break
print(m)
