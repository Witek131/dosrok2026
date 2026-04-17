from array import array


def f(n):
    while n > 0:
        if n % 10 == 7 and n != 7:
            return True
        else:
            return False


def f1(n):
    s = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if f(i):
                s.append(i)
            if f(n//i):
                s.append(n // i)

    if s:
        return min(s)
k = 0

for i in range(700_000, 150000000):
    if f1(i):
        print(i, f1(i))
        k+=1
    if k == 8:
        break