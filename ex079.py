# FEITO POR MIM
'''opcao = ' '
cont = 0
valores = list()
while opcao not in 'Nn':
    num = int(input(f"Digite {'um' if cont <= 1 else 'outro '} número: "))
    cont += 1
    if num in valores:
       print(f'Esse número já está na lista não vai ser adicionado!')
    else:
        valores.append(num)
        print(f'Valor registrado com sucesso...')
    opcao = str(input('Quer continuar? [S/N]: ')).strip()[0]
    while opcao not in 'NnSs':
        opcao = str(input('Quer Continuar? [S/N]: ')).strip()[0]
valores.sort()
print('=-' * 30)
print(f'Os numeros cadastrados são: {valores}')'''
# Feito pelo Guanabar
numeros = list()
while True:
    n= int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print(f'Valor duplicado! Não vou duplicar...')
    r = str(input("Quer continuar? [S/N]: "))
    if r in 'Nn':
        break
print('=-' * 30)
numeros.sort()
print(f"{'':^5}Você digitou os valores {numeros}")