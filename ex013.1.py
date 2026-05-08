produto = float(input('Entroduz o preço do produto: R$'))
parcial = produto - (produto * 8 / 100)
definitivo = produto - (produto * 20 / 100)
print('O preço do produto é de {:.2f}R$,\n 0 pagamento parcial com 15% de desconto é que vale: {:.2f}.\n Pagamento definitivo com 20% de desconto é que vale: {:.2f}R$'.format(produto,parcial,definitivo))
 