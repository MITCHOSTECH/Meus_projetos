from datetime import datetime
ano_atual = datetime.now().year
dados = dict()
dados['nome'] = str(input(f'Nome: ')).strip()
dados['ano'] = ano_atual - int(input(f'Ano de nascimento: '))
dados['ctps'] = int(input(f'Carteira de Trabalho (0 não tem): '))

if dados['ctps'] > 0:
    dados['contrato'] = int(input(f'Ano de Contratação: '))
    dados['salario'] = float(input(f'Salário: R$'))
    dados['aposentadoria'] = dados['ano'] + ((dados['contrato'] + 35) - datetime.now().year)
    for k, v in dados.items():
        print(f'  - {k} tem o valor {v}')
else:
    for k, v in dados.items():
        print(f'  - {k} tem o valor {v}')