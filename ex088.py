from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print(f'{'JOGA MEGA SENA':^30}')
print(f'-' * 30)
quant = int(input(f'Quantos jogos você quer que eu sorteie: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    jogos.sort()
    tot += 1
print('-=' * 3, f'Sorteando {quant} jogos', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(2)
print('-=' * 5, 'Boa Sorte', '-=' * 5)
