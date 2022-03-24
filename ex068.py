from random import randint
print('VAMOS JOGAR PAR OU ÍMPAR')
c = randint(0,10)       #randomização da escolha do computador
vit = 0                 #contador de vitórias
while True:
    v = int(input('Escolha um valor: '))
    e = ' '                 #espaço vazio para testar a variável escolha
    while e not in 'PI':    #teste de variável
        e = str(input('Escolha Par ou Ímpar? [P/I]: ')).strip().upper()
    t = v+c
    if t % 2 == 0:      #se o total das variáveis 't' e 'c' for igual a 0 ela é par, se não, é ímpar
        print(f'Você jogou {v} e o computador {c}. Total de {t} DEU PAR!')
    else:
        print(f'Você jogou {v} e o computador {c}. Total de {t} DEU ÍMPAR!')
    if e == 'P':        #teste da variável escolha
        if t % 2 == 0:  #se o total for par, e a escolha foi par, o usuário venceu
            print('Você VENCEU!')
            vit += 1    #vitória soma mais 1
        else:           #se o total for ímpar, e a escolha foi par, o usuário perdeu
            print('Você PERDEU!')
            break       #flag de parada
    elif e == 'I':      #teste da variável escolha
        if t % 2 == 1:  #se o total for ímpar, e a escolha foi ímpar, o usuário venceu
            print('Você VENCEU!')
            vit += 1    #vitória soma mais 1
        else:           #se o total for par, e a escolha foi ímpar, o usuário perdeu
            print('Você PERDEU!')
            break       #flag de parada
    print('Vamos Jogar Novamente ...')
print(f'GAME OVER! Você venceu {vit} vezes.')


