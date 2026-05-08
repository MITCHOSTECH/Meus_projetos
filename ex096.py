"Feito por mim"
'''def area(larg, comp):
    s = larg * comp
    print(f'Dimensão do terreno tem {larg} largura e {comp} de comprimento: A area totsl do Terreno é de {s}m²')


area(float(input('Largura: ')),float(input('Comprimento: ')))'''

def area(larg, comp):
    a = larg * comp
    print(f'A área de um Terreno {larg} x {comp} é de {a}m².')


#Programa principal
print(' Controle de Terrenos')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)