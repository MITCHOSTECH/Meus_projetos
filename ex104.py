#FEITO POR MIM
'''
def leiaInt(numero):
    while True:
        numero = input(f'Digite um número: ')
        if numero.isnumeric():
            print(f'\033[34mVocê digitou o número {numero}\033[m')
            break
        else:
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')





#Programa  Principal
print(15 * "-")
n = leiaInt('Digite um número: ')
'''

# FEITO PELO GUANBARA
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0:31mErro! digite um n;umero inteiro válido.\033[m')
        if ok:
            break
    return valor
#Programa principal
n = leiaInt(f'Digite um número: ')
print(f'Você acabou de digitar o número {n}')
