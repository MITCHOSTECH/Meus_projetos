from math import radians, tan, sin,cos

ângulo = float(input('Digite o angolo que voce Quer: '))
seno = sin(radians(ângulo))
coseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))

print('O ângulo de {} tem o seno de {:.2f}\n Coseno de {:.2f} \n Tangente {:.2f}'.format(ângulo, seno, coseno, tangente))
