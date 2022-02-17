k = float(input('Quantos kms o carro percorreu? '))
d = int(input('Por quantos dias ele foi alugado? '))
print('O valor total a ser pago é de R${:.2f}'.format((k * 0.15) + (d * 60)))
