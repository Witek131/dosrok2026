print(f'{2047:b}', int('100000000000', 2))
prog = {(' ', 0): (' ', -1, 1),
        (' ', 1): ('1', -1, 2),
        ('0', 1): ('1', 2, 1),
        ('1', 1): ('0', -1, 1),
        (' ', 2): (' ', 2, 2)}


def mt(s):
    s = list(' ' + s + ' ')
    q = 0
    i = -1
    while True:
        print(int(''.join(s), 2))
        cmd = prog[s[i], q]
        s[i] = cmd[0]
        if cmd[1] == 2: break
        i += cmd[1]
        q = cmd[2]
    return ''.join(s)


res = mt(f'{2047:b}')

print(int(res, 2), res)
