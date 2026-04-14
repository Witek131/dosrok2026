from itertools import *
k = 0
for i in product('АЕЛПРЬ', repeat = 5):
    a = ''.join(i)
    k+=1
    if k%2 == 0 and a[0] !='Ь' and a[0] != 'Р' and a.count('Л') >= 2:
        print(k, a)
