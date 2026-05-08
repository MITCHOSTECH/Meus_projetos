soma = 0 # iniciar váriavel aucumulativa, acomulação dos valores
cont = 0 # iniciar váriavel contador para saber quantas vezer encontrou o resultado com forme a condição
for c in range(1,501,2):
    if c % 3 == 0:
        cont += 1  # De acordo com a condição acima esta certa ou True o  contador adiciona +1 para saber quantas execução serta foram feita para chegar a soma em baixo
        soma += c # a soma de todos os valores
print(f'A soma de todos os {cont}  valores solicitados é : {soma}')
