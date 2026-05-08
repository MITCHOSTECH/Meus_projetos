dados_jogador = dict()
partidas = list()
dados_jogador['nome'] = str(input(f'Nome do jogador: ')).strip()
tot = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou: '))
for c in range(0, tot):
    partidas.append(int(input(f'Qantos golo na partida {c+1}: ')))
dados_jogador['golos'] = partidas[:]
dados_jogador['total'] = sum(partidas)
print("-=" * 30)
print(dados_jogador)
print('-=' * 30)
for k, v in dados_jogador.items():
    print(f' {k} tem valor {v}')
print('-=' * 30)
print(f'O jogador {dados_jogador["nome"]} jogou {len(dados_jogador["golos"])} partidas')
for i, v in enumerate(dados_jogador['golos']):
    print(f'   => Na partida{i}, Fez {v} golos.')
print(f'Foi no total de {dados_jogador["total"]}')
