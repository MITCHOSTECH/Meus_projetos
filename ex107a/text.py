import moeda


p = float(input(f'Digite um preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}R$')
print(f'O dobro de {p} é {moeda.dobro(p)}R$')
print(f'Aumento de 10%, temos {moeda.aumentar(p,10)}R$')
print(f'Reduzindo a 13%, temos {moeda.diminuir(p,13)}R$')

