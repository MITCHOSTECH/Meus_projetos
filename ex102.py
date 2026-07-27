#FEITO POR MIM

#def fatorial(n, show = True):
"""
    3 aspas

    :param n: número fatorial
    :param show: (Opcional) Mostrar ou não o processo dod resultados
    :return: fatorial

    3 aspas

    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show is True:
            print(f'{n} x {c -1}',end=" ")
    return f"\n={f}"
    #print(f'\n={f}')

# Programa principal
num = int(input(f'Número fatorial: '))
print('-' * 18)
print(f"O fatórial de {num}")
print(fatorial(num,False))
"""

#FEITO PELO PROF GUNABARA
def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: o número a ser calculado.
    :param show: (opcão) mostre ou não a conta.
    :return: o valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f



print(fatorial(5, show=True))
help(fatorial)