def aumentar(preco = 0, taxa = 0):
    res = preco + (preco * taxa) / 100
    return res


def diminuir(preco = 0, taxa = 0):
    res = preco - (preco * taxa / 100)
    return res



def dobro(preco = 0):
    res = preco * 2
    return res



def metade(preco = 0):
    res = preco / 2
    return res

def moeda(preco = 0, moeda = 'R$'):
    return f"{moeda}{preco:.2f}".replace('.',',')

def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}'.center(30))
    print(f'Dobro do preço:  \t{moeda(dobro(preco))}'.center(30))
    print(f'Metade do preço: \t{moeda(metade(preco))}'.center(30))
    print(f'{taxaa}% de aumento: \t{moeda(aumentar(preco, taxaa))}'.center(30))
    print(f'{taxar}% de redução:  \t{moeda(diminuir(preco, taxar))}'.center(30))
    print('-' * 30)
    print('Volte sempre!')