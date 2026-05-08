'''from random import randint
from operator import itemgetter
sorteio = dict()
print('Valores sorteados: ')
for c in range(1,5):
    sorteio[f'{' ':7}O jogador{c}'] = f'{randint(1,11)}'
for k, v in sorteio.items():
    print(f'{k}  tirou {v} no dado')
print(f'{"-=" * 30}')
print(f'   ==Ranking dos jogadores ==)'''

# FEITO PELO GUANABARA
from random import randint
from time import sleep
from operator import itemgetter
jogo = { 'jogador1': randint(1,6),
         'jogador2': randint(1,6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ranking = list()
print(f'Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print(f'{"-=" * 30}')
print(f'  == O Ranking dos jogadores == ')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
