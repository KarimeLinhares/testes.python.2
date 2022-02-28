from time import sleep

print('-=' * 20)
print('Números pares existentes entre 1 e 50.')
print('-=' * 20)
for c in range(2, 51, 2):
    print(c, end=' ')
    sleep(0.5)
print('FIM!')
