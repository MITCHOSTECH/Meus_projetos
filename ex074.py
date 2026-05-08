''''from random import choice
cincos_numeros = (2,4,10,212,211,21,2,1)
cont = igual =  1
maior = menor = inicio = 0
for numeros_gerado in cincos_numeros:
    aleatoria = choice(cincos_numeros)
    print(f'O números {cont} aleatória da tupla: {aleatoria}')
    cont += 1
    inicio += 1
    if inicio == 1:
        maior = aleatoria
        menor = aleatoria
    else:
        if aleatoria > maior:
            maior = aleatoria
        elif aleatoria < menor:
                menor = aleatoria
print(f'O maior valor gerado pela tupla é {maior}\n O menor valor gerado pela tupla é: {menor}')'''
from random import randint
n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
# print(f"Eu sortiei o valor {n}") O valor pode ser executado com print ou com for
print(f"Os valores solteado são: ",end='')
for elemento in n:
    print(f"{elemento} ",end='')
print(f"\nO maior valor soterado foi {max(n)}")
print(f"O menor valor sorteado foi {min(n)}")