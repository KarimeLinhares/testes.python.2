n = input('Digite o nome de uma cidade: ').strip()
print('O nome da cidade escolhida é {}'.format(n))
print('Essa cidade começa com Santo?: {}'.format(n[:5].upper() == 'SANTO'))
