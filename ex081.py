valores = list()
opcao = ' '

while opcao not in 'Nn':
    num = int(input('Digite um valor: '))
    valores.append(num)
    opcao = str(input('Quer continuar? [S/N]: ')).strip()[0]
    while opcao not in 'NnSs':
        opcao = str(input('Quer continuar? [S/N]: ')).strip()[0]
print(f"a) Foram digitado: {len(valores)} {'numero' if len(valores) <= 1 else 'numeros'}")
valores.sort(reverse=True)
print(f"b) Lista em ordem decrescente: {valores}")
if 5 in valores:
    print("c) O número cinco foi encontrado na lista")
else:
    print("c) O número cinco não foi digitado")
