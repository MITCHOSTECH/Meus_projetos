def aumentar(preco=0, taxa = 0, formatacao=False):
    '''
    -> Calcular o aumento do preço de produto.
    :param preco: Valor  do produto.
    :param taxa: Aumento de percentagem de preco do produto.
    :param formatacao:(Opção) verificar se o produto vai ou não ser convertido?
    :return:
    '''
    res = preco + (preco * taxa / 100)
    return res if formatacao is False else moeda(res)


def diminuir(preco=0, taxa = 0, formatacao=False):
    res = preco - (preco * taxa / 100)
    return res if formatacao == False else moeda(res)


def dobro(preco = 0,formatacao=False):
    res = preco * 2
    return res if not formatacao else moeda(res)



def metade(preco=0, formatacao=False):
    res = preco / 2
    return res if not formatacao else moeda(res)


def moeda(preco,tipo="€"):
    return f"{preco:.2f}{tipo}".replace('.',',')

def resumo(preco = 0, taxaa=20, taxab = 10):
    print('-' * 30)
    print(f'RESUMO DE VENDA'.center(30))
    print(f'-' * 30)
    print(f'{taxaa:}% de aumento:{moeda(aumentar(preco,taxaa)):->15}'.center(30))
    print(f'{taxab}% de desconto: \t{moeda(diminuir(preco, taxab))}'.center(30))
    print(f'O dobro de {moeda(preco)}: \t {moeda(dobro(preco))}'.center(30))
    print(f'A metade de {moeda(preco)}: \t{moeda(metade(preco))}'.center(30))