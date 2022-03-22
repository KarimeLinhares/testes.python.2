t = 'S'     #o valor para continuar o teste é 'S'
c = s = m = maior = menor = 0   #todas as variáveis iniciam no programa com o valor 0
while t == 'S':     #teste de loop, enquanto o valor for 'S', ele irá continuar no loop
    n = int(input('Digite um número: '))
    c += 1          #o contador somará sempre mais 1
    s += n          #os números de n, serão somados para dar a média no final
    if c == 1:                  #para iniciar o teste de maior ou menor número, o contador começa em 1
        maior = menor = n       #por não haver número maior ou menor, essas variáveis vão receber os valores de 'n'
    else:                       #havendo valores ...
        if n > maior:           #se a variável 'n' for o número maior, ela receberá a variável maior
            maior = n
        if n < menor:           #se a variável 'n' for o número menor, ela receberá a variável menor
            menor = n
    t = str(input('Deseja continuar? [S/N]: ')).upper().strip()
m = s/c     #após a soma dos valores de 'n', a divisão é feita por fora para melhor compreensão
print('Você digitou {} números e a média foi {} '.format(c, m)) #'c' é o contador e 'm' a média
print('O maior valor foir {} e o menor foi {}'.format(maior, menor))    #maior é o maior número e menor o menor número.