print('-' * 39)
print(f'{"LISTAGEM DE PREÇOS":^40}') # CENTRALIZAR O TEXTO
print('-' * 39)
listagem_produto = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.00,'Estojo',25.00,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)
for pos in range(0, len(listagem_produto)):
    if pos % 2 == 0:
        print(f"{listagem_produto[pos]:.<30}", end=' ')# a função :30(espaçamento  30 vezes de cada produto em [pos]= posição) A função < ( o símbolo inferior é para colocar todos os nomes de produto alinhado pela esquerda) . (O ponto é para preencher o 30 espaçamento em pontos ......
    else:
        print(f"R${listagem_produto[pos]:>7.2f}")
print('-' * 40)