#FEITO POR MIM
print(f'#=' * 8 +'Tabuada'+ 8 * '#= ')
numero = int(input('Digite número de casa(TABUADA):' ))
inicio = 0
fim = 10
for c in range(inicio,fim):
    inicio += 1
    print(f'''[ {inicio}] x [{numero}] = {inicio * numero}''')
print('FIM DA OPERAÇÃO')

#FEITO PELO PROFESSOR
num = int(input('Digite um número para ver sua tabuada: '))
for cont in range(1,11):
    print('{} x {:2} = {}'.format(num,cont,num * cont))