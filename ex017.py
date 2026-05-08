'''Feito por Mim '''
'''
from math import sqrt
a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor cateto adjacente: '))

h = (a**2) + (b**2)
r = sqrt(h)
print('O valor da hipotenusa é {:.2f}'.format(r))
'''
# Feito por Professor
from math import hypot
co = float(input('COMPRIMENTO DO CATETO OPOSTO: '))
ca = float(input('O COMPRIMENTO DO CATETO ADJACENTE: '))
# hi = (co ** 2 + ca ** 2) ** (1/2)
hi = hypot(co, ca)
print('A hipotenusa vai me dir {:.2f}'.format(hi))
