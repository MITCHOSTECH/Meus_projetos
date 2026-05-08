dados_pessoas = list()
pessoas = dict()
opcao = ' '
while opcao not in 'N':
    pessoas['nome'] = str(input(f'Nome: ')).strip().upper()
    pessoas['sexo'] = str(input(f'Sexo? [M/F]: ')).strip().upper()[0]
    while pessoas['sexo'] not in 'MF':
        print(f'Erro tente novamente... [M/F]')
        pessoas['sexo'] = str(input(f'Sexo: ')).strip().upper()[0]
    pessoas['idade'] = int(input(f'Idade: '))
    dados_pessoas.append(pessoas.copy())
    opcao = str(input(f'Quer continuar? [S/N]: ')).strip().upper()[0]
    while opcao not in 'NS':
        print(f'Erro tente novamente... [S/N]')
        opcao = str(input(f'Quer continuar? '))

print(dados_pessoas)
print(pessoas)

