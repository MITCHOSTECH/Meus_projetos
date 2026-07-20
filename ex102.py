def fatorial(n, show = True):
    '''

    :param n: número fatorial
    :param show: (Opcional) Mostrar ou não o processo dod resultados
    :return: fatorial
    '''
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show is True:
            print(f'{n} x {c}',end=" ")
    return f"\n={f}"
    #print(f'\n={f}')

# Programa principal
num = int(input(f'Número fatorial: '))
print('-' * 18)
print(f"O fatórial de {num}")
print(fatorial(num,False))