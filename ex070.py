'''print('-' * 30)
print(' ' * 7,'LOJA BARATO')
total_gasto = produtos_mais_d_mil = comparacao = produto_mais_barato = 0
novo_produto = ''
while True:
    print('-' * 30)
    produto = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('preço: R$'))
    total_gasto += preco
    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    comparacao += 1
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if preco > 1000:
        produtos_mais_d_mil += 1
    if comparacao == 1:
        produto_mais_barato = preco
        novo_produto = produto
    else:
        if preco < produto_mais_barato:
            produto_mais_barato = preco
            novo_produto = produto
    if opcao == 'N':
        break
    print('-' * 30)
    print(' ' * 6,'NOVO PRODUTO')
print('-' * 30)
print(f'O Total gasto na compra é de \033[1:34m{total_gasto:5.2f}R$\033[m\nTemos \033[1:34m{produtos_mais_d_mil}\033[m que custam mais de \033[1:31mR$1000\033[m\nO nome do produto mais barato é {novo_produto} produtos que custa \033[1:34m{produto_mais_barato:5.2f}R$\033[m')
print('FIM DO PROGRAM!')
'''
#FEITO PELO GUANABARA
total = totmil  = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    if preco > 1000:
        totmil += 1
    if cont == 1: #ou if totmil == 1 or preco < menor :Dessa nao é preciso executar o bloco else. obs: executa se 1 estrução  num é iqual a 1 ou si preço < menor.
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp == 'N':
            break
print(f'O total da compra foi {total:6.2f}R$')
print(f'Temos {totmil} produtos custando mais de 1000R$.')
print(f'O nome do produto mais barato é {barato}')