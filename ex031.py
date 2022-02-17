d = int(input('Digite a distância da viagem em km: '))
if d <= 200:
    print('O valor total da sua passagem será de: R${}'.format(d*0.50))
else:
    print('O valor da sua passagem será de: R${}'.format(d*0.45))
