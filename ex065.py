menor = maior = media = num_div = soma = n =  0
opcao = ''
while opcao in 's':
    n = int(input('Digite um número qualquer?:'))
    num_div +=1
    soma += n
    if num_div == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opcao = str(input('Quer continuar[S/N]?: ')).lower().strip()[0]
media = soma / num_div
print(f'A média {media} número introduzido {num_div} o maior número {maior} e o menor {menor}')