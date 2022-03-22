n = c = s = 0       #os valores das variáveis 'n', 'c' e 's', iniciam com 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:     #999 é o flag, ou valor de parada
    c += 1          #o contador vai sempre somar mais 1, para que eu tenha a quantidade de valores escolhidos
    s += n          #a soma dos valores escolhidos menos o 999
    n = int(input('Digite um número [999 para parar]: '))   #colocando a variável 'n' no início e dentro do while, faz com que o valor 999 não seja lido
print('Você digitou {} números e a soma entre eles foi {}.'.format(c, s))