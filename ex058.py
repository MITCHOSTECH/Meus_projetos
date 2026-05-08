#FEITO POR MIM
from random import randint
print('''UM JOGO ENTRE O COMPUTADOR E O JOGADOR
 ONDE O JOGADOR INTRODUZE UM NÚMERO SE O NUMERO FOR IGUAL
 AO COMPUTADOR <<VENCEU>> CASO ACONTRÁRIO <<PERDEU>> O COMPUTADOR VENCEU!''')
computador = randint(0, 10)
jogador = int
tentativas_falhadas = 1
while computador != jogador:
    jogador = int(input('Digite um número interiro qualquer?: '))
    if jogador == computador:
        print('venceu')
    else:
        tentativas_falhadas += 1
        print('Tenta mais...')
print(f'VENCEU mais precisa de ({tentativas_falhadas}) tentativas para vencer o computador')
# FEI PELO GUANABARA
'''from random import randint
computador = randint(0,10)
print('Sou eu Computador.... Acabei de pensar em um número entre 0 e 10')
print('Será que voce consegue advinhar qual foi: ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Menos... Tente mais uma vez.')
        else:
            print('Mais... Tente mais uma vez.')
print(f'Aceitou com {palpites} tentativas')
'''
