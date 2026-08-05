from ex108a import moeda


p = float(input(f'Digite um preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}R$')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}R$')
print(f'Aumento de 10%, temos {moeda.moeda(moeda.aumentar(p,10))}R$')
print(f'Reduzindo a 13%, temos {moeda.moeda(moeda.diminuir(p,13))}R$')

