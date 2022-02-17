v = float(input('Qual é o valor da casa?: '))
s = float(input('Qual é o valor do salário do comprador?: '))
a = int(input('Em quantos anos o comprador pretende pagar?: '))
p = v/a
print('O valor das parcelas que deverão ser pagas é de R${:.2f} em {} anos!'.format(p, a))
po = s*30/100
print('O valor de 30% do salário do comprador é de R${:.2f}'.format(po))
if po <= s:
    print('Empréstimo concedido! O valor das parcelas será de R${:.2f} em {} anos!'.format(p, a))
else:
    print('NEGADO! O valor da parcela é maior do que 30% do salário do comprador!')
print('Tenha um bom dia!')



