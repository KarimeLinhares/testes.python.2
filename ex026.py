f = input('Digite uma pequena frase: ').upper().strip()
print('A letra A aparece {} vezes'.format(f.count('A')))
print('O primeiro A está posicionado no caracter de numero: {}'.format(f.find('A')+1))
print('O último A está posicionado no caracter de número: {}'.format(f.rfind('A')+1))
