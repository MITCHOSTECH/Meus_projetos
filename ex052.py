#FEITO POR MIM
'''numeros_inteiros = int(input('Digite um número inteiro qualquer?: '))

if numeros_inteiros % 1 == 0 and numeros_inteiros %  numeros_inteiros == 0 and numeros_inteiros % 2 != 0:
    print(f'0 número {numeros_inteiros} é um número <<PRIMO>> porque: {numeros_inteiros}/1 = {numeros_inteiros / 1:.0f} com o resto de {numeros_inteiros % 1 } valor e também {numeros_inteiros}/{numeros_inteiros}= {numeros_inteiros / numeros_inteiros:.0f} com o resto de {numeros_inteiros % numeros_inteiros} \n obs: Números primos: são os números inteiros com dois divisores.')
elif numeros_inteiros % 1 == 0 and numeros_inteiros % numeros_inteiros == 0 and numeros_inteiros % 2 == 0:
    print(f'O número {numeros_inteiros} não é um número <<PRIMO>>\n \033[1:31mOBS: OS NÚMEROS DITO NÃO PRIMOS SE TÊM MAIS DE 3 DIVISORES\033[m')'''
# FEITO PELO PROFESSOR GUANABARA
num  = int(input('Digite um número?: '))
numeros_divisiveis = 0
for c in range(1,num + 1):
    if num % c == 0:
        numeros_divisiveis += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\033[mO número {num} foi divisível {numeros_divisiveis} vesez ')
if numeros_divisiveis == 2:
    print('E por isso é <<PRIMO>>')
else:
    print('E por isso não é <<PRIMO>>')
