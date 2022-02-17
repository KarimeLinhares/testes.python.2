l = float(input('Coloque a largura da parede: '))
a = float(input('Agora coloque a altura dessa parede: '))
#m2 = l*a
print('Os valores de largura e altura da sua parede são de: {}m e {}m.'.format(l, a))
print('Sabendo disso, a área dessa parede é de: {}m², e portanto,'
      '\na quantidade de tinta necessária para a pintura é de {:.2f}l.'.format(l*a, (l*a)/2))