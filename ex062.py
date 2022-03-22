'''from time import sleep
print('=-'*35)
print('Escolha o Primeiro Termo e a Razão logo abaixo para calcular uma PA.')
print('=-'*35)
t = int(input('Caso queira continuar digite 1\nSe quiser sair, digite 0: ')) #testa se o usuário quer continuar o programa ou não.
while t == 1:                           #enquanto o teste for igual a 1, entra-se no loop
    print('\nIniciando ...')
    sleep(1)
    pt = int(input('\nPrimeiro Termo: ')) #vairável do primeiro termo
    r = int(input('Razão: '))           #variável da razão
    termo = pt                          #o 'termo' vai receber o número escolhido pelo usuário como primeiro termo
    c = 1                               #o contador começa com o número 1
    print('CALCULANDO!')
    print('=-'*6)
    sleep(1)
    while c <= r:
        sleep(0.5)
        print('{} - '.format(termo), end='')
        termo += r                      #o termo é a soma dele próprio com a razão
        c += 1                          #o contador sempre soma mais 1
    print('Fim!')
    sleep(1)
    print('...reiniciando...')
    sleep(2)
    print('=-' * 35)
    print('Escolha o Primeiro Termo e a Razão logo abaixo para calcular uma PA.')
    print('=-' * 35)
    t = int(input('Caso queira continuar digite 1\nSe quiser sair, digite 0: '))  #testa novamente se o usuário quer continuar
if t == 0:          #se o teste for 0, o programa finaliza
    print('\nSaindo do programa ...')
sleep(2)
print('\nPrograma Finalizado!')'''

print('GERADOR DE PA')
pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
termo = pt  #o 'termo' vai receber o número escolhido pelo usuário como primeiro termo
c = 1       #o contador começa com o número 1
t = 0       #total de termos que o usuário quer mostrar
s = 10      #simulação em que o usuário escolha mais 10 termos
while s != 0:   #teste de loop, enquanto a variável 's' for diferente de zero, o programa vai continuar
    t = t + s   #o total recebe a soma da variável total mais a variável soma
    while c <= t: #enquanto o contador for menor ou igual ao total de termos, ele seguirá contruindo a PA
        print('{} - '.format(termo), end='')
        termo += r   #o termo é a soma dele com a variável razão
        c += 1       #o contador irá adcionar sempre mais 1
    print('PAUSA')
    s = int(input('Quantos termos você quer mostrar a mais?: '))
print('Programa finalizado com {} termos aos total.'.format(t))   #Se o usuário escolher 0, o programa vai terminar
