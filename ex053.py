'''f = str(input('Escreva uma frase: ')).strip().upper() #opção com for
p = f.split()
j = ''.join(p)
inv = ''
for l in range(len(j) -1, -1, -1):
    inv += j[l]
print(j, inv)
if inv == j:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')'''

f = str(input('Digite uma frase: ')) #opção com fatiamento
p = f.split()
j = ''.join(p)
inv = j[::-1]
print('O inverso de {} é {}'.format(j, inv))
if inv == j:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')



