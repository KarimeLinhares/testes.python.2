vp = float(input('Digite o valor do produto: '))
vpd1 = vp*10/100
vpd2 = vp*5/100
vpa = vp*20/100
print('Agora escolha a forma de pagamento:')
print('-=-'*20)
mp = int(input('Digite 1 para à vista\nDigite 2 para à vista no cartão\n'
               'Digite 3 para parcelamento em 2x \nOu digite 4 para parcelamento em três ou mais vezes: '))
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
    print('O valor do produto parcelado no cartão será de R${:.2f}'.format(vp))
else:
    print('Você escolheu pagamento parcelado em 3x ou mais!')
    print('O valor do produto parcelado em 3x ou mais será de R${:.2f}, pois terá acréscimo de 20%!'.format(vp + vpa))

print('\nObrigado por comprar conosco! Tenha um bom dia!')


