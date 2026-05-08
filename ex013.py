salário = float(input('Qual é o seu vencimento?: R$'))
novoSalário = salário + (salário * 15 / 100)
print('O salário actual do funconário é de {:.2f}R$, com o aumeto de 15%.\n o novo salário é :{:.2f}R$'.format(salário,novoSalário))