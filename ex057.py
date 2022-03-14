'''sexo = 'M'
while sexo == 'M' or sexo == 'F':
    sexo = str(input('Você é homem ou mulher? [M/F]: ')).upper()
    if sexo == 'M':
        print('Sexo registrado como masculino')
    if sexo == 'F':
        print('Sexo registrado como feminino')
while sexo != 'M' and sexo != 'F':
    print('Você digitou errado, tente novamente')'''

sexo = str(input('Informe seu sexo [M/F]: ')).upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()
print('Sexo {} registrado com sucesso'.format(sexo))


