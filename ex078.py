#Feito por mim
'''valores = list()
for c in range(0, 4):
    valores.append(int(input(f'Digite o {c + 1} valor: ')))

maior = max(valores)
menor = min(valores)
print(f'O maior valor digitado foi: {maior} encontrado na posição ',end='')
for pos, v in enumerate(valores):
    if v == maior:
        print(f'{pos + 1}..',end='')
print(f'\nO menor valor digitado foi: {menor} encontrado na posição: ',end='')
for pos, v in enumerate(valores):
    if v == menor:
        print(f' {pos + 1}...',end='')
print('\nFim de programa.\nVolte sempre!')

'''
# Feito pelo prof Guanabara
listaNum = []
maior = menor = 0
for c in range(0, 5):
    listaNum.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        maior = menor = listaNum[c]
    else:
        if listaNum[c] > maior:
            maior = listaNum[c]
        if listaNum[c] < menor:
            menor = listaNum[c]
print(f"Você digitou os valores {listaNum}")
print(f'O maior digitado foi {maior} nas posicões ',end='')
for pos, valor in enumerate(listaNum):
    if valor == maior:
        print(f'{pos}...',end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ',end='')
for pos, valor in enumerate(listaNum):
    if valor == menor:
        print(f'{pos}...',end='')
print()
