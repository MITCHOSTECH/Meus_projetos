def leiaDinheiro(msg):
    while True:
        n = str(input(msg)).strip().replace(',', '.')
        if n.count('.') <= 1 and n.replace('.', '').isnumeric():
            res =  float(n)
            break
        #try:
        #   return float(n)
        #except ValueError:
        else:
            print(f'\033[31mERRO: "{n}" é um preço inválido!\033[m')
    return res

msg = 'Digite o preço: €'


