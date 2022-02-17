a = int(input('Digite o ano de nascimento do atleta: '))
i = (2022 - a)-1
print('O atleta nasceu em {} e portanto tem {} anos'.format(a, i))
if i <= 9:
    print('A categoria desse atleta é MIRIM, pois ele tem {} anos'.format(i))
elif 10 <= i <= 14:
    print('A categoria desse atleta é INFANTIL, pois ele tem {} anos'.format(i))
elif 15 <= i <= 19:
    print('A categoria desse atleta é JUNIOR, pois ele tem {} anos'.format(i))
elif i == 20:
    print('A categoria desse atleta é SÊNIOR, pois ele tem {} anos'.format(i))
else:
    print('A categoria desse atleta é MASTER, pois ele tem {} anos'.format(i))
