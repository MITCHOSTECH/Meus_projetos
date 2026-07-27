#FEITO POR MIN (Sem usar dicionário)
"""def notas(*n, sit = True ):
    quant = len(n)
    maior = menor = soma = media = 0
    for pos, nota in enumerate(n):
        if pos == 0:
            maior = menor = nota
        if nota > maior:
            maior = nota
        else:
            if nota < menor:
                menor = nota
        soma += nota
    media = soma / quant
    situacao = ""
    if sit:
        if media > 7:
            situacao = "BOA"
        else:
            if  media > 6 :
                situacao = "Razuavel"
            if media < 5:
                situacao = "RUIN"
    if situacao == "":
        situacao = "Desativado"
    return f'a) Quantidade(s) nota(s): {quant}\nb) Maior nota: {maior}\nc) Menor nota: {menor}\nd) Média da turma: {media}\ne) Situação: {situacao}'



# PROGRAMA PRINCIPAL
resp = notas(10, 5.5, 6.5, 12, sit = True)
print(resp)"""

#FEITO PELO GUANABARA
def notas(*n,sit=False ):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não indicar a situação.
    :return: Dictionário com vários informações sobre a situação da turma.
    """
    from math import floor
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = floor(sum(n)/len(n))
    if sit:
        if r['média'] >= 7:
            r['situação'] = "Boa"
        elif r['média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'

    return r


#PROGRAMA PRINCIPAL
resp = notas(9, 10, 5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)