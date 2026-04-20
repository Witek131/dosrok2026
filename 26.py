def f(x,y):
    return (84882!=4*y+3*x) or (a<x) or (x<y)

d = []
for x in range(1,100000):
    y = (84882-3*x)//4
    if y>0: d.append([x,y])
m = []
#for a in range(1,100000,1000):
for a in range(1,23000):
    if all(f(x,y)==1 for x,y in d):
        m.append(a)
print(max(m))
# 12125