def f(n):
    while n>0:
        if n%10== 7:
            return True
        else:
            return False

for i in range(700_000, 150000000):
    if f(i) and