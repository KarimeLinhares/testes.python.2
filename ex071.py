print('BANCO\n')
v = int(input('Qual o valor que deseja sacar?\nR$'))
t = v       #o total recebe o valor escolhido pelo usuário
ced = 50    #o valor de cédula mais alto é 50
c = 0       #o contador recebe 0
while True:
    if t >= ced:     #se o total for maior que 50, ele vai retirar cédulas, até acabar o valor daquela respectiva cédula, e contar quantas cédulas foram retiradas
        t -= ced
        c += 1
    else:
        if c > 0:
            print(f'A quantidade de cédulas de R${ced:.2f} é de {c}')
        if ced == 50:   #o valor de cédulas vai diminuir a medida que não sejam mais necessárias até o contador chegar a 0. Se o valor chegar a zero o programa para.
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        c = 0
        if t == 0:
            break