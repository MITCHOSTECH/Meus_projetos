# Feito po mim
par = list()
impar = list()
valores = list()
opcao = ' '
while opcao not in 'Nn':
    numeros = int(input("Digite um valore: "))
    valores.append(numeros)
    valores.sort()
    if numeros % 2 == 0:
        par.append(numeros)
    elif numeros % 2 != 0:
        impar.append(numeros)
    opcao = str(input(f"Quer continuar? [S/N]: ")).strip()[0]
    while opcao not in 'NnSs':
        opcao = str(input(f"Quer continuar? [S/N]: ")).strip()[0]
print(f"Os valores introduzidos na lista formam: {valores}")
print(f"Os valores pares digitados foram: {par}")
print(f"Os valores impares digitados foram: {impar}")