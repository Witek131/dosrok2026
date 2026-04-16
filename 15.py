def f(a1, a2, x):
    p = 25 <= x <= 64
    q = 40 <= x <= 115
    a = a1 <= x <= a2
    return p <= ((q and (not a)) <= (not p))

h = []
for i in (25,64,40,115):
    h.append(i)
    h.append(i+ 0.1)
    h.append(i - 0.1)
d = []
for a1 in h:
    for a2 in h:
        if a1<=a2 and all(f(a1, a2 , x) for x in h):
            d.append(a2 - a1)
print(min(d))
