import modulo

p = float(input('Digite o preço: €'))
print(f'O aumento de 15% é {modulo.moeda(modulo.aumentar(p, 15))} ')
print(f'O desconto de 20% é {modulo.moeda(modulo.diminuir(p, 20))}')
print(f'O dobro de {modulo.moeda(p)} é {modulo.moeda(modulo.dobro(p))}')
print(f'A metade de {modulo.moeda(p)} é {modulo.moeda(modulo.metade(p))}')