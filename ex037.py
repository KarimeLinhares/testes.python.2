n = int(input('Digite um número: '))
print('''Escolha uma das bases para a conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
o = int(input('Sua opção: '))
if o == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif o == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
else:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))

