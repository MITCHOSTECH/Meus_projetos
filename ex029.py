from time import sleep
motorista = str(input('Nome da motorista se faz favor:  ')).strip()
velocidade_carro = float(input('Em que velocidade esta por hora:  '))

multa= velocidade_carro - 80
pagar_multa = multa * 7

sleep(2)
if velocidade_carro > 80:
    print('O sr. {} tem multa de {}km a mais, foi indiciado com a multa de {}€ com a validade de 5 dias úteis'.format(motorista, multa, pagar_multa))
else:
    print('O Sr. {} esta de PARANÉNS, continunação de uma boa tarde e um bom trabalho'.format(motorista))
