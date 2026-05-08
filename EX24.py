'''' FEITO POR MIM
cidade = str(input('Digite o nome da sua cidade: '))
dividir = cidade.split()
procurar_palavra = dividir[0].upper()
print('SANTO' in procurar_palavra)'''

cid = str(input('Em que cidade você nasceu?: ')).strip()
print(cid[:5].upper() == 'SANTO')