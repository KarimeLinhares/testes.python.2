from random import randint
from time import sleep
l = ('PEDRA', 'PAPEL', 'TESOURA')
c = randint (0,2)
e = int(input('''\033[1;94;47m Vamos jogar Jokenpô!\033[m 
Escolha uma das opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
A sua escolha é: '''))
print('-='*14)
print('\033[1;33mJO...\033[m')
sleep(1)
print('\033[1;33mKEN...\033[m')
sleep(1)
print('\033[1;31mPÔ!!!\033[m')
sleep(0.5)
print('-='*14)
print('O computador escolheu \033[1;36m{}\033[m'.format(l[c]))
print('O jogador jogou \033[1;35m{}\033[m'.format(l[e]))
print('-='*14)
if c == 0:
    if e == 1:
        print('O Jogador \033[1;32mVENCEU!\033[m')
    elif e == 2:
        print('O Computador \033[1;32mVENCEU!\033[m')
    elif e == 0:
        print('\033[1;33mEMPATE!\033[m')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!\033[m')
elif c == 1:
    if e == 0:
        print('O Computador \033[1;32mVENCEU!\033[m')
    elif e == 1:
        print('\033[1;33mEMPATE!\033[m')
    elif e == 2:
        print('O Jogador \033[1;32mVENCEU!\033[m')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!\033[m')
elif c == 2:
    if e == 0:
        print('O Jogador \033[1;32mVENCEU!\033[m')
    elif e == 1:
        print('O Computador \033[1;32mVENCEU!\033[m')
    elif e == 2:
        print('\033[1;33mEMPATE!\033[m')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!\033[m')
else:
    print('\033[1;31mJOGADA INVÁLIDA!\033[m')







