for i in range(2, 100):
    s = f'{i:b}'
    s = s + str(s.count('1') % 2)
    s = s + str(s.count('1') % 2)
    r = int(s, 2)
    if r > 253:
        print(i)
