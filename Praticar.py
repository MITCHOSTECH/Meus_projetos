from random import randint
from time import sleep

def sortear(lista):
    for c in range(0,5):
        lista.append(randint(1, 10))
    print(f'Os números sorteados são: ', end=" ")
    for num in lista:
        print(f"{num}", end=" ")
        sleep(1)
    print()



def SomarPar(lista):
    soma = 0
    print(f'Números paraes sorteados são: ', end=" ")
    for num in lista:
        if num % 2 == 0:
            print(f"{num}", end=" ")
            sleep(1)
            soma += num
    print(f',Soma dos números pares: [{soma}]')



numeros = list()
sortear(numeros)
SomarPar(numeros)