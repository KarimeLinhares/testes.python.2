import random
'''print('Vamos fazer uma brincadeira, eu vou escolher um número de 0 a 10')
ce = random.randint(0,10)
e = int(input('E agora, em qual número você acha que eu pensei?: '))
while ce > e:
    e = (int(input('Mais, tente de novo: ')))
    if ce < e:
        e = (int(input('Menos, tente de novo: ')))
    if ce == e:
        print('Você acertou! Eu também pensei no {}. Parabéns!'.format(ce))'''

computador = random.randint(0,10)
print('Sou seu computador ... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais ... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos ... Tente mais uma vez.')
print('Eu pensei no número {}. Você acertou com {} tentativas. Parabéns!'.format(computador, palpites))

