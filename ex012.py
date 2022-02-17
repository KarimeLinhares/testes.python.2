p=float(input('Digite o valor que deseja conferir: '))
po= p*5/100
print('O valor escolhido foi {} reais, '
      'esse valor com o desconto de 5% fica {:.2f} reais.'.format(p, p-po))