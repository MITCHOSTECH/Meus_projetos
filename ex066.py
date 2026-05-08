'''n = int(input('digite um número inteiro?: '))
n_digitado = soma = 0
while n != 999:
    n_digitado +=1
    soma += n
    n = int(input('Digite un número inteiro?: '))
print(f'Número digitsdo {n_digitado} a soma total dos números {soma}')'''
# Melhor forma
n = n_digitado = soma = 0
while n != 999: # Ou pode ser True = que é uma condição de repitição infinito
    n = int(input('Digite un número inteiro?: '))
    if n == 999:
        break
    n_digitado +=1
    soma += n
print(f'Número digitsdo são: {n_digitado} a soma total dos números {soma}')