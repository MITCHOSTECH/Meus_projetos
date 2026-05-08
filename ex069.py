print('-' * 40)
print(' ' * 10,'CADASTRE UMA PESSOA')
maior_d_idade = homens_cadestrado = mulheres_menor_vinte = 0
while True:
    print('-' * 40)
    nome = str(input('Nome Completo: ')).strip().upper().split()[0]
    idade = int(input('Idade: '))
    sexo = str(input('Genero: ')).strip().upper()[0]
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Genero:')).strip().upper()[0]
    if idade >= 18:
        maior_d_idade += 1
    if sexo == 'M':
        homens_cadestrado += 1
    if sexo == 'F':
        if idade < 20:
            mulheres_menor_vinte += 1
    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
    print('-' * 40)
    print('NOVO CADASTRO:')
print('-=' * 10)
print('=======FIM DO PROGRAMA=======!')
print(f'Total de pessoas com mais de 18 anos : \033[1:34m{maior_d_idade}\033[m\nNo total foram cadestrado \033[1:34m{homens_cadestrado}\033[m Homens\nE temos \033[1:34m{mulheres_menor_vinte}\033[m mulheres com menos de 20 anos')
print('Volte Sempre.')
#FEITO PELO GUANABARA
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo? [M/F]: ')).strip().upper()[0]
    if tot18 >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'M' and sexo < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoa com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} Homens cadastrado')
print(f'E temos {totM20} Mulheres com menos de 20 anos de idade')
print('VOLTE SEMPRE!')