n1 = float(input('Digite um número aleatóriamente: '))
n2 = float(input('Digite o segundo número aleatóriamente:  '))
n3 = float(input('Digite o terceiro número aleatóriamente: '))

'''maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
    print('o NUMERO MAIS MAIOR E',maior)
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
    print('O numero mais menor E',menor)
'''
maior = max(n1,n2,n3)
menor = min(n1,n2,n3)

print('O número mais grande é {}, O mais pequeno é {}'.format(maior,menor))