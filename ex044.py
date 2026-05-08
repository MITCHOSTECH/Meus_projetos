from datetime import date
from time import sleep
print('{:*^50}'.format(' LOJA CALIPIMBUTH '))
produto = float(input('Preso da compra?: €'))
condicao_pagamento = int(input('\033[1:34m(1). \033[mÀ vista DINHEIRO / CHEQUE: \033[1:35mdesconto de 10% \033[m \n\033[1:34m(2). \033[mÀ visa no\033[1:34m Cartão\033[m:\033[1:35m5% de desconto\033[m.\n\033[1:34m(3). \033[mEm até\033[1:34m2x no cartão\033[m:Preço normal.\n\033[1:34m(4). 3x ou mais \033[mo cartão:\33[1:35m20%\033[m de juros.\n Escolhe uma das condições?: '))
data_actual = date.today()

print('Ano',data_actual,'\nprocessar...')
sleep(3)
if condicao_pagamento == 1:
    desconto1 = produto - (produto * 10 / 100)
    print('Novo preço do produto \033[1:34m{:.2f}€\033[m com Desconto de \033[1:35m10%\033[m'.format(desconto1))
elif condicao_pagamento == 2:
    desconto2 = produto - (produto * 5 / 100)
    print('Novo preço do produto \033[1:34m{:.2f}€\033[m com desconto de \033[1:35m5%\033[m'.format(desconto2))
elif condicao_pagamento == 3:
    resultado = produto / 2
    print('\033[1:34:40mO preço será parcelada em 2x\033[m vai custar {:.2f}€ SEM JUROS'.format(resultado))
elif condicao_pagamento == 4:
    parcela = int(input('Quantas parcelas: '))
    juros = produto + ( produto * 20/100)
    calcular_parcela =  juros / parcela
    print('Tem \033[1:35m20 %\033[m de juros equivale \033[1:34m{:.2f}€\033[m\nA sua compra sera parcelada em \033[1:34m{}x de {:.2f}€\033[m'.format(juros,parcela,calcular_parcela))
else:
    print('\033[1:31m OPÇÃO INVÁLIDA DE PAGAMENTO TENTA NOVAMAENTE!')