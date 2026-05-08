'''dados_Pss = dict()

dados_Pss['Nome'] = str(input(f'Nome: ')).strip().upper()
dados_Pss['Media'] = float(input(f'Média de {dados_Pss['Nome']}: '))
if dados_Pss['Media'] >= 7 :
    dados_Pss['Situação'] = 'Aprovado'
else:
    dados_Pss['Situação'] = 'Reprovado'
for k, v in dados_Pss.items():
    print(f'{k} é igual a {v}')'''

# FEITO PELO GUNABARA

aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip().upper()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print(f'-=' * 30)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')