print('-='*20)
print('Analisador do triangulo')
print('-='*20)
r1 = float(input('primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimeto: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As funções podem formar um triângulo')
else:
    print('Os funções não podem formar um triângulo')