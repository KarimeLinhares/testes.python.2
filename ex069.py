print('CADASTRO DE PESSOAS')
cm = ci = cf = 0        #contadores sempre começam com 0
while True:
    print('CADASTRO')
    idade = int(input('Idade:'))
    sexo = ' '      #teste de validação de sexo
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo == 'M':     #contador de sexo masculino
        cm += 1
    if idade > 18:      #contador de maiores de 18 anos
        ci += 1
    if sexo == 'F' and idade < 20:      #contador de mulheres com menos de 20 anos
        cf += 1
    cont = ' '      #teste de validação da continuação
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if cont == 'N':     #flag de parada
        break
print(f'Total de pessoas com mais de 18 anos: {ci}')
print(f'Ao todo temos {cm} homens cadastrados')
print(f'E temos {cf} mulheres com menos de 20 anos.')