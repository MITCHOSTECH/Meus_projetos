#FEITO POR MIM
from datetime import date
data_hoje = date.today().year
print(f'hoje o ano: {data_hoje}')
maior = 0
menor = float('inf')
for contar in range(1,6):
    peso = float(input('Quanto quilo pesas: '))
    if maior < peso:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O menor é {menor} e o maior é {maior}')
# FEITO PELO GUSTAVO GUANABARA
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input(f'Peso do {p} pessoa:'))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}kg')
print(f'O  menor peso lido foi {menor}kg')