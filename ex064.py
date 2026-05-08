# FEITO POR MIN ERRADO
'''n_inteiro = int(input('Digite número inteiro?:'))
c = 999
numeros_digitados = 0
soma = 0
while c != n_inteiro:
    n_inteiro = int(input('Digite número inteiro?: '))
    numeros_digitados +=1
    if c != n_inteiro:
        if c == n_inteiro:
            print('FIM')
print(f'Foi digitado {numeros_digitados} números com a soma no total de: {n_inteiro}')'''
#FEITO PELO GUANABARA
cont = soma = 0
num = int(input('Digite um número [condição de parage: 999]: '))
while num != 999:
    soma+=num
    cont += 1
    num = int(input('Digite um número [condição de parage: 999]: '))
print(f'Você digitou {cont} números e a soma entre eles são {soma}')
#print(f'Você digitou {cont-1} números e a soma entre eles são {soma - 999}') pode ser resolvido assim eliminando contador - 1 e a somma -999 para eliminar ou poderia ser resolvido que a soma+=-999