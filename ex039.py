a = int(input('Em que ano o jovem nasceu?: '))
i = (2022 - a)-1
print('A idade do jovem é de {} anos!'.format(i))
if i > 18:
    print('Você já passou o período do alistamento militar!')
    print('O alistamento deveria ter sido feito a {} anos atrás!'.format(i - 18))
elif i == 18 or i == 17:
    print('Chegou a hora de fazer o alistamento militar!')
else:
    print('Ainda não está na hora de se alistar!')
    print('Faltam {} anos para o seu alistamento'.format(18 - i))



