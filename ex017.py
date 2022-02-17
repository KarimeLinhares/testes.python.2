from math import hypot
co = float(input('Coloque o valor do cateto oposto: '))
ca = float(input('Coloque o valor do cateto adjacente: '))
ch = hypot(co, ca)
print('O valor da hipotenusa é igual à {:.2f}'.format(ch))

'''co = float(input('Coloque o valor do cateto oposto: '))
ca = float(input('Coloque o valor do cateto adjacente: '))
ch = (co**2 + ca**2)**(1/2)
print('O valor da hipotenusa é igual à {:.2f}.'.format(ch))'''

