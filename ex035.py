a = int(input('Digite o valor do primeiro comprimento: '))
b = int(input('Agora digite o valor do segundo: '))
c = int(input('Agora digite o valor do terceiro: '))
if a < b + c and b < a + c and c < a + b:
    print('É um triângulo!')
else:
    print('Não é um triângulo!')

