from datetime import datetime
nascimento = int(input('Que ano  quer analisar? Coloqua 0 para analisar o ano atual: '))
if nascimento == 0:
    nascimento = datetime.now().year
if nascimento % 4 == 0 and nascimento % 100 !=0 or nascimento % 400 == 0:
    print('O ano {}  é o ano BISSEXTO'.format(nascimento))
else:
    print('O ano {} nao é BISSEXTO'.format(nascimento))
print('OBRIGADO PELO SEU TEMPO')