altura = float(input('Entre a altura da parede em metro?: '))
largura = float(input('Entre a largura em metro?: '))

area = altura * largura
print('A sua parede tem a dimensão de {}x{} e a sua área é de {}m2 '.format(altura,largura,area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))