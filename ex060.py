#primeira opção
'''n = int(input('Digite um número para calcular o seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''

#segunda opção
'''from math import factorial
v = int(input('Digite um número para calcular o seu Fatorial: '))
c = v
print('Calculando {}! = '.format(v), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print('{}'.format(factorial(v)))'''

#terceira opção
from math import factorial
v = int(input('Digite um número para calcular o seu fatorial: '))
c = v
print('Calculando {}! = '.format(v), end='')
for z in range(v):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print('{}'.format(factorial(v)))


