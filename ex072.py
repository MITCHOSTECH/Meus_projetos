#FEITO POR MIM
'''while True:
    num_extenso = ('Zerro','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezasseis','Dezassete','Dezoito','Dezenove','Vinte')
    num_digitado = int(input('Digite um número intediro entre 0 a 20: '))
    while  num_digitado < 0 or num_digitado > 20:
        num_digitado = int(input('Digite um número inteiro entr 0 a 20: '))
    for numeros in num_extenso:
        print(f'O volor digitado é {num_extenso[num_digitado]}')
        break
    break
'''
# FEITO PELO GUANABARA
condicao = ' '
num = 0
num_extenso = ('Zerro','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze',
               'Doze','Treze','Quatorze','Quinze','Dezasseis','Dezassete','Dezoito','Dezenove','Vinte')
while condicao not in 'N':
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'O número digitado é {num_extenso[num]}')
    else:
        print('Tente novamente!')
    condicao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
print('FIM DO PROGRAMA!')
