matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
som_par = som_coluna = maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
print("=-" * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]",end="")
        if matriz[coluna][linha] % 2 == 0:
            som_par += matriz[linha][coluna]
    print()
print("-=" * 30)
print(f"A soma dos numeros pares são: {som_par}")
for coluna in range(0,3):
    som_coluna += matriz[coluna][2]
print(f"A soma dos valores da terceira coluna é {som_coluna} ")
for linha in range(0, 3):
    if linha == 0:
        maior = matriz[1][linha]
    else:
        if matriz[1][linha] > maior:
            maior = matriz[1][linha]
print(f"O maior número da segunda linha é {maior}")
