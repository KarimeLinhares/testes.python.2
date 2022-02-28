from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range (1,8):
    ano = int(input('Em que ano nasceu a {}º pessoa: '.format(c)))
    id = atual - ano
    if id >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E {} pessoas menores de idade'.format(totmenor))





