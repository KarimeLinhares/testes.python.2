v1 = int(input('Qual o primeiro número?: '))
v2 = int(input('Qual o segundo número?: '))
print('Os números escolhidos são {} e {}!'.format(v1, v2))
if v1 > v2:
    print('O número {} é maior do que {}!'.format(v1, v2))
elif v2 > v1:
    print('O número {} é maior do que {}!'.format(v2, v1))
else:
    print('Os dois números são iguais!')
