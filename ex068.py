from random import randint
print('-=' * 15)
print(' ' * 5,'JOGO PAR IMPAR',' ' * 5)
resultado = ''
condicao = ''
usuario_valor = 0
vitoria = 0
while resultado != 'PERDEU':
    print('-=' * 15)
    usuario_valor = int(input('Digite um valor: '))
    computador = randint(1, 10)
    p_i = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    while p_i != 'P' and p_i != 'I':
        p_i = str(input('Par ou Ímpar? [P/I]:')).strip().upper()[0]
    soma = computador + usuario_valor
    if soma % 2 == 0:
        if p_i == 'P':
            resultado = 'VENCEU'
            condicao = 'PAR'
            print('-' * 20)
            print(f'Você jogou {usuario_valor} e o computador {computador}. Total de {usuario_valor + computador} DEU {condicao}')
            print('-' * 20)
            print('VENCEU!\nVamos jogar novamente..')
            vitoria += 1
        else:
            resultado = 'PERDEU'
            condicao = 'PAR'
            print('-' * 20)
            print(f'Você jogou {usuario_valor} e o computador {computador}. Total de {usuario_valor + computador} DEU {condicao}')
            print('-' * 20)
            print(f'{resultado}')
    else:
        if soma % 2 != 0:
            if p_i == 'I':
                resultado = 'VENCEU'
                condicao = 'ÍMPAR'
                print('-' * 20)
                print(f'Você jogou {usuario_valor} e o computador {computador}. Total de {usuario_valor + computador} DEU {condicao}')
                print('-' * 20)
                print(f'Você {resultado}\nVamos jogar novament...')
                vitoria += 1
            else:
                resultado = 'PERDEU'
                condicao = 'ÍMPAR'
                print('-' * 20)
                print(f'Você jogou {usuario_valor} e o computador {computador}. Total de {usuario_valor + computador} DEU {condicao}')
                print('-' * 20)
                print(f'Você {resultado}')
print('-=' * 23)
print(f'GAME OVER! Você venceu {vitoria} vezes!')
