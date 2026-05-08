print('=+' * 31)
print('=-' * 10,'\033[1:34mTabuada Curso em video\033[m','-='*10)
cont = 0
opcao = ''

while opcao in 'Ss':
    print('=+' * 31)
    tabuada = int(input('\033[1:32mDigite tabuada de qualquer número inteiro?\033[m:'))
    if tabuada < 0:
        print('FIM DE TABUADA')
        break
    for cont in range(1,10):
        print(f'                \033[34m{cont}\033[m x \033[32m{tabuada}\033[m = {cont * tabuada}')
        cont += 1
    print('-=' * 31)
    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()
print('PROGRAMA DE TABUADA INCERADO! **VOLTE SEMPRE**')