# FEITO PO MIM
pessoas = dict()
dados = list()
opcao = " "
while opcao not in 'N':
    pessoas['nome'] = str(input('Nome: ')).strip().upper()
    pessoas['sexo'] = str(input('Sexo? [M/F]: ')).strip()[0]
    while pessoas['sexo'] not in 'mMfF':
        print('ERRO! Responde apenas Feminino ou Masculino')
        pessoas['sexo'] = str(input('Sexo? [M/F]: ')).strip().upper()[0]
    pessoas['idade'] = int(input('Idade: '))
    dados.append(pessoas.copy())
    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while opcao not in 'NS':
        print('ERRO! Digite Sim ou Não.')
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
print(f'{"=>":^5}Foram cadastrado no total: {len(dados)} {"Pessoa" if len(dados) <= 1 else "Pessoas"}')
media_idade = 0
mulheres = list()
idade_acima = list()
for i, ps in enumerate(dados):
    media_idade += ps['idade']
    if ps['sexo'] in 'fF':
        mulheres.append(ps)
print(f'{"=>":^5}A média de idade do grupo é de: {media_idade/ (len(dados))} Anos')
print(f'{'==':^5}As listas com todas as Mulheres ==')
for i, m in enumerate(mulheres):
    print(f'Dados da {i + 1}º Pessoas: {m['nome']}')
print(f'{'==':^5}Lista das pessaos com idade acima da média: ')
for i, ps in enumerate(dados):
    if ps['idade'] >= media_idade /len(dados):
        idade_acima.append(ps)
for i, pm in enumerate(idade_acima):
    print(f"{'':^5}Id {i} Nome: {pm["nome"]} Sexo: {pm["sexo"]} Idade: {pm["idade"]}")

