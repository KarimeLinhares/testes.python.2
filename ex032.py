'''import calendar
a = int(input('Digite um ano qualquer: '))
an = calendar.isleap(a)
if an == True:
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto!')'''

from datetime import date
a = int(input('Digite um ano qualquer. Caso queira usar o ano atual, digite 0: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 !=0 or a % 400 == 0:
    print('O ano {} é Bissexto!'.format(a))
else:
    print('O ano {} não é bissexto!'.format(a))

