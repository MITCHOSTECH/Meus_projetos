from time import sleep
from datetime import date

numero = int(input('Entre qualquer número reias: '))
escolha = int(input('Escolhe as operações seguinte para conversão: \n1 => Converter em número Binário.\n2 => Converter em octal.\n3 => Converter em hexadecimal.\n'))
data_actual = date.today().year

print('processando...')
sleep(4)

if escolha == 1:
    print('A conversão do número {} em Binário é: {}'.format(numero,bin(numero)[2:]))
elif escolha == 2:
    print('A conversão do número {} em octal é: {}'.format(numero,oct(numero)[2:]))
elif escolha == 3:
    print('A conversão do número {} em hexadecimal é: {}'.format(numero,hex(numero)[2:]))
else:
    print('O senhor escolheu a opção invalida!')
print('exelentíssimo pela vossa confiança desde sempre até {}'.format(data_actual))