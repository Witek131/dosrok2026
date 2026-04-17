def f(x, y, p):
    if (x + y) >= 65: return p % 2 == 0
    if p ==0:
        return 0
    h = [f(x + 1, y, p - 1), f(x, y + 1, p - 1), f(x, y * 3, p - 1), f(x * 3, y, p - 1)]
    return any(h) if p % 2 == 1 else any(h)


print([i for i in range(1, 59) if f(i, 6, 2)])
print([i for i in range(1, 59) if f(i, 6, 3) and not f(i, 6, 1)])
print([i for i in range(1, 59) if f(i, 6, 4) and not f(i, 6, 2)])
