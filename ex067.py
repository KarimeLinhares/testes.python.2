while True: #loop infinito
    n = int(input('Quer ver a tabuada de qual valor? [Caso queira sair, digite um número negativo]: '))
    if n < 0:   #flag de parada
        break
    for c in range(1, 11):  #'for' usado, pois eu tenho um número de início e fim definido
        print(f'{n} X {c:2} = {n * c:2}')
print('Programa de Tabuada encerrado! Volte Sempre!')
