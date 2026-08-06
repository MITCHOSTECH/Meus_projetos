import modulo

p = float(input('Digite o preço: €'))
print(f'O aumento de 15%:  \t{modulo.aumentar(p, 15,True)} ')
print(f'O desconto de 20%: \t{modulo.diminuir(p, 20, True)}')
print(f'O dobro de {modulo.moeda(p)}: \t{modulo.dobro(p,True)}')
print(f'A metade de {modulo.moeda(p)}:\t{modulo.metade(p,True)}')