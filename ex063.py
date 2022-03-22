#A Sequência de Fibonacci é uma série comum e freqüentemente usada em Matemática. É mostrado abaixo.
#0,1,1,2,3,5,8,13,21,34,55,89,144,229....

n = int(input('Quantos termos você quer mostrar?: '))
t1 = 0  #o primeiro termo da sequência de fibonacci é igual a 0
t2 = 1  #o segundo termo da sequência de fibonacci é igual a 1
print('{} - {} - '.format(t1, t2), end='')      #gambiarra pra que ele mostre sempre os dois primeiros termos como 0 e 1
c = 3       #o contador precisa começar em 3, pois 2 termos já existem
while c <= n:   #enquanto o contador for menor que o número de termos escolhido pelo usuário, ele fará a progressão
    t3 = t1 + t2    #o terceiro valor é a soma dos dois primeiros
    print('{} - '.format(t3), end='')
    t1 = t2     #Simulação de transferência de valor para a soma do próximo (o valor de t2, vira o valor de t1 e etc)
    t2 = t3     #Simulação de transferência de valor para a soma do próximo (o valor de t3, vira o valor de t2 e etc)
    c += 1
print('FIM!')

