def notas(*n, sit = True ):
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






resp = notas(10, 5.5, 6.5, 12, sit = True)
print(resp)