print('10 TERMOS DE UMA PA')
pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
d = pt + (11 - 1) * r
for c in range(pt, d, r):
    print(c, end=' ')
print('FIM!')
