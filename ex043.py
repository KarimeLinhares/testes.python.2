p = float(input('Digite o valor do seu peso em Kg: '))
a = float(input('Digite o valor da sua altura em m: '))
imc = p/a**2
print('Os valores do seu peso e altura são respectivamente {:.1f}kg e {:.2f}m'.format(p, a))
print('Calculando o valor, o seu IMC é igual {:.2f} m²'.format(imc))
if imc < 18.50:
    print('O valor do seu IMC é classificado como baixo peso.')
elif imc > 40.00:
    print('O valor do seu IMC é classificado como obesidade mórbida.')
elif 30.00 <= imc <= 40.00:
    print('O valor do seu IMC é classificado como obesidade.')
elif 25.00 <= imc <= 30.00:
    print('O valor do seu IMC é classificado como sobrepeso.')
else:
    print('O valor do seu IMC é classificado como peso ideal.')



