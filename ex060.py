# FEITO POR MIM
'''fatorial = int(input('Digite o fatorial de qualquer número inteiro?: '))
resultado = 1

for c in range(1,fatorial+1):
    resultado *= c
print(f' fatorial de {fatorial} = {resultado}')'''

'''from math import factorial
fatorial = int(input('Digite o fatorial de qualquer números inteiro?: '))
print(f'O factorial de {fatorial}! = {factorial(fatorial)}')
'''
#FEIRO PELO GUANABARA
n = int(input('Digite um número para calcular seu fatorial: '))
c= n
f = 1
print(f'Calculando {n}! = ',end='')
while c > 0:
    print(f'{c}',end='')
    print(' x ' if c > 1 else ' = ',end='')
    f*=c
    c -= 1
print(f'{f}')