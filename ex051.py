primeiro_termo = int(input('Digite o termo?:'))
razao = int(input('Digite a Razão?:'))
decimo_termo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo_termo + razao , razao):
    print(f'{c}',end=' -> ')
print('ACABOU')
