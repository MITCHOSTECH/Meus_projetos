def aumentar(preco, taxa, formatacao=False):
    res = preco + (preco * taxa / 100)
    return res if formatacao is False else moeda(res)


def diminuir(preco, taxa, formatacao):
    res = preco - (preco * taxa / 100)
    return res if formatacao == False else moeda(res)


def dobro(preco,formatacao):
    res = preco * 2
    return res if not formatacao else moeda(res)



def metade(preco, formatacao):
    res = preco / 2
    return res if not formatacao else moeda(res)


def moeda(preco,tipo="€"):
    return f"{preco:.2f}{tipo}".replace('.',',')