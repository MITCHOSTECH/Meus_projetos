 produto = float(input('Introduza um preço?:R$ '))
resultado = produto - (produto * 5 / 100)


print('O preço introduzido do produto é : {:.2f}€, Que tem como desconto 5%,\n O preço actual é de: {:.2f}€'.format(produto,resultado))
