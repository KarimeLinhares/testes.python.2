n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('A primeira nota do aluno foi {} e a segunda {}.'.format(n1, n2))
m = (n1 + n2) / 2
if m < 5.0:
    print('O aluno teve nota {}, está REPROVADO!'.format(m))
elif m >= 7.0:
    print('O aluno teve nota {}, está APROVADO!'.format(m))
else:
    print('O aluno teve nota {}, está de RECUPERAÇÃO!'.format(m))
