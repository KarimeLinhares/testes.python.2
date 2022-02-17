a = float(input('Digite o valor do primeiro lado: '))
b = float(input('Digite o valor do segundo lado: '))
c = float(input('Digite o valor do terceiro lado: '))
if c+b < a or a+c < b or a+b < c:
    print('Não é um triângulo.')
elif a == b and a == c:
    print('Este triângulo possui todos os lados iguais, portanto, é um triângulo EQUILATERO!')
elif a == b or b == c or c == a:
    print('Este triângulo tem dois lados iguais, portanto, é um triângulo ISÓCELES!')
else:
    print('Este triângulo possui todos os lados diferentes, portanto, é um triângulo ESCALENO!')
