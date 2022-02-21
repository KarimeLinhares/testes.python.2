a = float(input('Digite o valor do primeiro lado: '))
b = float(input('Digite o valor do segundo lado: '))
c = float(input('Digite o valor do terceiro lado: '))
if a < b+c and b < a+c and c < a+b:
    print('É um triângulo!', end=(' '))
    if a == b and a == c:
        print('E este triângulo possui todos os lados iguais, portanto, é um triângulo EQUILATERO!')
    elif a == b or b == c or c == a:
        print('E este triângulo tem dois lados iguais, portanto, é um triângulo ISÓCELES!')
    else:
        print('E este triângulo possui todos os lados diferentes, portanto, é um triângulo ESCALENO!')
else:
    print('Não é um triângulo.')