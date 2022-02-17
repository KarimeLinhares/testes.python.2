s = float(input('Digite o valor do seu salário atual: '))
sp1 = s*10/100
sp2 = s*15/100
if s >= 1250:
    print('O aumento no seu salário será de 10%: R${:.2f}'.format(s+sp1))
else:
    print('O aumento no seu salário será de 15%: R${:.2f}'.format(s+sp2))
