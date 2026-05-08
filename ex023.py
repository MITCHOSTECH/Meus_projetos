# FEITO POR MIM
'''n = str (input('Digite um número com 4 digíto: ')).strip()

print('Unidade: {} \ndezena: {} \ncentena: {} \nmilhar: {}'.format(n[3],n[2],n[1],n[0]))'''

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))