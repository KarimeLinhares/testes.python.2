'''n = int(input('Digite um número para ver sua tabuada: '))
print('-=' * 6)
for c in range(1,11):
    m = c*n
    print('{:2} X'.format(c), end='')
    print('{:2} ='.format(n), end='')
    print('{:3}'.format(m))
print('-=' * 6)
print('FIM!')'''

n = int(input('Digite um número para ver a sua tabuada: ')) #melhor opção
print('-=' * 6)
for c in range (1, 11):
    print('{} x {:2} = {:2}'.format(n, c, n*c))
print('-=' * 6)
print('FIM!')




