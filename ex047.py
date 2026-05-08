''' Primeira passo
for c in range(1,51,):
    if c % 2 == 0:
        print(c)
'''
# Outra maneira / segundo passo:
inicio = 0
fim = 51
print(f'Os números pares de {inicio} e {fim} sã0:')
for i in range(inicio,fim,2):
    print(f' {i}')