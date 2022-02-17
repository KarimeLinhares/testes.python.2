n = int(input('Digite um valor de 0 a 9999: '))
print('O número escolhido foi {}'.format(n))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade:{}'.format(u))
print('dezena:{}'.format(d))
print('centena:{}'.format(c))
print('milhar:{}'.format(m))
