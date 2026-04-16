f = dict()
for i in range(1, 270000):
    if i <10:
        f[i] = 3
    else:
        f[i] = (i+4) *f[i-5]
print((f[257487] / 683 + 67 * f[257477])/ f[257472])
