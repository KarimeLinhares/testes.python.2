from time import sleep
e = 0
sair = False
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('digite o segundo valor: '))
while not sair:
    print('-='*15)
    print('[ 1 ] somar\n'
          '[ 2 ] multiplicar\n'
          '[ 3 ] maior\n'
          '[ 4 ] novos números\n'
          '[ 5 ] sair do programa')
    print('-='*15)
    e = int(input('>>> Qual é a sua opção?: '))
    if e == 1:
        print('A soma entre {} + {} é {}'.format(v1, v2, v1 + v2))
    elif e == 2:
        print('A multiplicação entre {} x {} é {}'.format(v1, v2, v1*v2))
    elif e == 3:
        if v1 > v2:
            print('O número maior entre {} e {} é {}'.format(v1, v2, v1))
        if v2 > v1:
            print('O número maior entre {} e {} é {}'.format(v1, v2, v2))
    elif e == 4:
        print('Deseja escolher novos números?')
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('digite o segundo valor: '))
    elif e == 5:
        sair = True
        print('Finalizando ...')
        sleep(1)
    else:
        print('Opção inválida. Tente de novo.')
        print('-=' * 15)
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('digite o segundo valor: '))
    sleep(1.5)
print('O programa acabou!')










