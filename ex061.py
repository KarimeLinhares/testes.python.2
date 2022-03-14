print('10 TERMOS DE UMA PA')
pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
termo = pt
c = 1
while c <= 10:
    print('{} - '.format(termo), end='')
    termo += r
    c += 1
print('Fim!')
