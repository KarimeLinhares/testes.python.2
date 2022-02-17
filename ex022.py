n = str(input('Digite o seu nome completo: ')).strip()
print('O Seu nome é: {}'.format(n))
print('O seu nome todo em maiúsculo fica: {}'.format(n.upper()))
print('O seu nome todo em minúsculo fica: {}'.format(n.lower()))
print('O número de letras ao todo é: {}'.format(len(n) - n.count(' ')))
n1 = n.split()
print('O número de letras do primeiro nome é: {}'.format(len(n1[0])))

#outra opção#print('O número de letras do primeiro nome é: {}'.format(n.find(' ')))



