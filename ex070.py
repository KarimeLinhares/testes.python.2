print('LOJA SUPER BARATÃO')
total = cp = menor = contador = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$ '))
    contador += 1
    total += preço
    if preço > 1000:
        cp += 1
    if contador == 1 or preço < menor:
        menor = preço
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print('FIM DO PROGRAMA!')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {cp} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi o(a) {barato} que custa R${menor:.2f}')
