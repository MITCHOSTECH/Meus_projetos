def leiaDinheiro(n):
    while True:
        n = str(input(f'Digite o preço: €')).strip()
        if n.isnumeric():
            res = float(n)
            break
        else:
            print(f'\033[31;1mERRO: [{n}] é um preço inválido!')
    return res




