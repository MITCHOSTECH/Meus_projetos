import modulo

p = float(input('Digite o preço: €'))
print(f'O aumento de 15% é {modulo.aumentar(p, 15)} ')
print(f'O desconto de 20% é {modulo.diminuir(p, 20)}')
print(f'O dobro de {p} é {modulo.dobro(p)}')
print(f'A metade de {p} é {modulo.metade(p)}')