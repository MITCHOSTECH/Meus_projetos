def ficha(n, g = 0):
    if n == "":
        n = "<<Desconhecido>>"

    # Não foi executado por que a função só deve executar ou processar os dados não converter (regra programador)
    """if g == "":
        g = "<<Desconhecido>>"
    else:
        g = int(g)"""
    print(f'O jogador {n} fez {g} golo(s) no campeonato')



nome = str(input(f'Nome do jogador: '))

golo = input(f'Golo do jogador: ')

#Execu'xão correta
if golo.isnumeric():
    golo = int(golo)
else:
    golo = 0

ficha(nome, golo)