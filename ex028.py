import random
print('Vamos fazer uma brincadeira, eu vou escolher um número de 0 a 5')
ce = random.randint(0,5)
e = int(input('E agora, em qual número você acha que eu pensei?: '))
if ce == e:
    print('Você acertou! Eu também pensei no {}. Parabéns!'.format(ce))
else:
    print('Você errou! Eu pensei no {}.'.format(ce))







