from datetime import date
inicio_menor = 0
inicio_maior  = 0


data_atual = date.today().year # extração da data atual
print(f'Hoje {data_atual}') # printação da data atual OUPUT!
for c in range(1,7+1):
    data_nascimento = int(input('Digite seu ano de nascimento (YYYY): '))
    total_ano_nascimento = data_atual - data_nascimento
    if total_ano_nascimento > 18:
        inicio_maior += 1 # concatenação em PyThon quer diver seguência somatória de 1 (variavel = variavel +1 = 2, variavel = variavel +1 = 3 sucessivamente)
        # ou (variavel += 1 = 2,variavel += 1 = 3 sucessivamente)
    elif total_ano_nascimento < 18:
        inicio_menor += 1

print('=*' * 17)
print(f'As pessoas maioritária: {inicio_maior}')
print(f'As pessoas menoritária: {inicio_menor}')
print('FIM DA OPERAÇÃO')
print('=+' * 17)