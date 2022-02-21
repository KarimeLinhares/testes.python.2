vp = float(input('Digite o valor do produto: R$ '))
vpd1 = vp*10/100
vpd2 = vp*5/100
vpa = vp*20/100
print('-=-'*20)
print('FORMAS DE PAGAMENTO!')
print('-=-'*20)
print('''[ 1 ] para à vista
[ 2 ] para à vista no cartão
[ 3 ] para parcelamento em 2x 
[ 4 ] para parcelamento em três ou mais vezes: ''')
mp = int(input('Digite a forma de pagamento escolhida: '))
print('-=-'*20)
if mp == 1:
    print('Você escolheu pagamento à vista!')
    print('O valor do produto à vista em dinheiro ou cheque será de R${:.2f}, pois terá 10% de desconto!'.format(
        vp - vpd1))
elif mp == 2:
    print('Você escolheu pagamento à vista no cartão!')
    print('O valor do produto à vista no cartão será de R${:.2f}, pois terá 5% de desconto!'.format(vp - vpd2))
elif mp == 3:
    print('Você escolheu pagamento parcelado em 2x!')
    print('O valor do produto parcelado no cartão será de R${:.2f} em 2x de R${:.2f}'.format(vp, vp/2))
elif mp == 4:
    print('Você escolheu pagamento parcelado em 3x ou mais!', end=(' '))
    p = int(input('Em quantas vezes você deseja dividir?: '))
    print('O valor do produto parcelado em {}x será de R${:.2f}, pois terá acréscimo de 20%! Cada parcela '
          'ficará no valor de R${:.2f}'.format(p, vp + vpa, (vp + vpa) / p))
else:
    print('Valor digitado não reconhecido, tente novamente.')
print('\nObrigado por comprar conosco! Tenha um bom dia!')


