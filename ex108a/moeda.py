def aumentar(preco = 0, taxa = 0, formatar=False):
    '''
    -> Calcular o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: O preço que se quer reajustar.
    :param taxa: qual é a porcentagem do aumento
    :param formatar:quer a saída formatada ou não?
    :return: O valor reajustado, com ou sem formato
    '''
    res = preco + (preco * taxa) / 100
    return res if formatar is False else moeda(res)


def diminuir(preco = 0, taxa = 0, formatar=False):
    res = preco - (preco * taxa / 100)
    return res if formatar == False else moeda(res)



def dobro(preco = 0, formatar=False):
    res = preco * 2
    return res if not formatar else moeda(res)



def metade(preco = 0, formatar=False):
    res = preco / 2
    return res if not formatar else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return f"{moeda}{preco:.2f}".replace('.',',')