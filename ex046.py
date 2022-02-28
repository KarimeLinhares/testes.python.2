from time import sleep
from emoji import emojize
print('-='*22)
print('Contagem Regressiva para a Queima de Fogos!')
print('-='*22)
for c in range (10, -1, -1):
    print(c)
    sleep(1)
print('BOOM!', end=' ')
print(emojize(':fireworks:'*5), end=' ')
print('BOOM!')




