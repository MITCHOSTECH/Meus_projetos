'''FEITO POR MIM
nome = str(input('Digite o nome completo: ')).strip()
dividir = nome.upper().split()
print('SILVA' in dividir)'''

nome = str(input('Qual é o seu nome: ')).strip()
print('O seu nome tem silva?: {}'.format('SILVA' in nome.upper()))