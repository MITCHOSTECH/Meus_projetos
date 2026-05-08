#FEITO POR MIM
'''from random import randint
numeros = list()

def sortear(* n):
    for num in n:
        print(f'{num}',end=" ")



def somarPar(n):
    par = list()
    contPar = 0
    for num in n:
        if num % 2 == 0:
            par.append(num)
            contPar += v
    print(f'{par}, temos uma soma total de {contPar}')

print('Os 5 números sorteados foram: ',end='')
for c in range(5):
    numero = randint(1, 11)
    numeros.append(numero)
    # sortaear(numeros) Erro! o porque em cada iteração a função vai guardar o primeiro número na segunda iteração vai copias ou pegar o número anterior mais o segundo número da iterr
sortear(numeros)
print('PRONTO!')

print('Somando valores Pares de: ',end="")
somarPar(numeros)
'''
# FEITO PELO GUANABARA
from random import randint
from time import sleep
def sortea(lista):
    print('Sorteando 5 valores da lista: ', end=" ")
    for c in range(5):
        n = randint(1,11)
        lista.append(n)
        print(f'{n}', end=" ", flush=True)
        sleep(0.3)

def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'\nSomando os valores pares de {lista}, temos {soma}')
numeros = list()
sortea(numeros)
somaPar(numeros)