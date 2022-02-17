from math import radians, sin, cos, tan
a = float(input('Digite o valor do ângulo: '))
s = sin(radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a, s))
c = cos(radians(a))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(a, c))
t = tan(radians(a))
print('O ângulo de {} tem a tangente de {:.2f}'.format(a, t))
