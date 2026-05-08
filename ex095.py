dados_jogador = dict()
partidas = list()
time = list()
while True:
    dados_jogador.clear()
    dados_jogador['nome'] = str(input(f'Nome do jogador: ')).strip()
    tot = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'{" ":^5}Qantos golo na partida {c+1}: ')))
    dados_jogador['golos'] = partidas[:]
    dados_jogador['total'] = sum(partidas)
    time.append(dados_jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in "SN":
            break
        print("ERRo! Responda apenas S ou N.")
    if resp in "N":
        break
print("-=" * 30)
print('cod',end=" ")
for i in dados_jogador.keys():
    print(f"{i:<15}", end="")
print()
print("-=" * 30)
for k, v in enumerate(time):
    print(f'{k:>3}',end=" ")
    for d in v.values():
        print(f'{str(d):<15}',end="")
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f"Levanta mento do jogador {time[busca]['nome']}")
        for i, g in enumerate(time[busca]['golos']):
            print(f'   No jogo {i + 1} fez {g} golos.')
    print("-" * 40)
print(f" << Volte Sempre >> ")