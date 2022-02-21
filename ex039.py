from datetime import date
at = date.today().year
a = int(input('Em que ano o jovem nasceu?: '))
i = (at - a)
print('A idade do jovem é de {} anos!'.format(i))
if i > 18:
    print('Você já passou o período do alistamento militar!')
    print('O alistamento deveria ter sido feito a {} anos atrás, mais precisamente em {}!'.format(i - 18, at - (i - 18)))
elif i == 18 or i == 17:
    print('Chegou a hora de fazer o alistamento militar!')
else:
    print('Ainda não está na hora de se alistar!')
    print('Faltam {} anos para o seu alistamento, ou seja, você deverá se alistar em {}'.format(18 - i, at + (18 - i)))




