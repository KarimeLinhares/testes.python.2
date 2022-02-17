v = int(input('Digite a velocidade do carro: '))
if v > 80:
    print('Você foi multado! Você excedeu o limite de velocidade!')
    mv = (v-80)*7
    print('Você terá de pagar R$ {:.2f} de multa'.format(mv))
print('Tenha um bom dia! Dirija com segurança!')


