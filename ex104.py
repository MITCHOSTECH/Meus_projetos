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
