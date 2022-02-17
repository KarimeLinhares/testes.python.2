s=float(input('Digite o salário atual do trabalhador: '))
so = s*15/100
print('O valor de salário atual é de {} reais, '
      'acrescentando 15% ele será de {:.2f} reais.'.format(s, s+so))
