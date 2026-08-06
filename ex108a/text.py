from ex108a import moeda


p = float(input(f'Digite um preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumento de 10%, temos {moeda.aumentar(p,10, True)}')
print(f'Reduzindo a 13%, temos {moeda.diminuir(p,13, True)}')

