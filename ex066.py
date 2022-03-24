c = s = n = 0  # as variáveis 'n', contador e a soma começam com 0
while True:  # enquanto o teste lógico for True, ele continuará rodando até o flag acontecer
    n = int(input('Digite um valor [Digite 999 para parar]: '))
    if n == 999:  # flag de parada
        break
    c += 1  # contador soma mais 1
    s += n  # soma dos valores de n
print(f'A soma dos {c} valores foi {s}!')  # f string
