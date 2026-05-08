from datetime import date
from time import sleep
peso = float(input('Quanto você pesa?: (kg) '))
altura = float(input('Qual é sua altura?: (m) '))
imc = peso / altura **2
print('Processar...')
sleep(1.4)
data = date.today()
print('Ano {}' .format(data))
if imc <= 18.5:
    print('ABAIXO DO PESO \nIMC= {:.2f}'.format(imc))
elif imc <= 25:
    print('PESO IDEAL \nIMC = {:.2f}'.format(imc))
elif 25 <= imc <= 30:
    print('SOBRE PESO \nIMC = {:.2f}'.format(imc))
elif 30 <= imc <= 40:
    print('OBESIDADE \nIMC = {:.2f}'.format(imc))
else:
    print('OBESIDADE MÓRBIDA {:.2f}'.format(imc))