from time import sleep
distancia_viagem = float(input('Qual é a distancia da viagem: '))
sleep(2)
print('Voce esta preste a comecar uma viagem.....')

if distancia_viagem  <=200:
    viagem_longa = distancia_viagem * 0.45
    print('O valor da sua viagem é de {}£'.format(viagem_longa))
else:
    pagar_viagem = distancia_viagem * 0.50
    print('O a sua viagem é de {}£'.format(pagar_viagem))
print('Boa viagem!')