inicio = 0
for c in range(0,6+1):
    numero = int(input('Digite qualquer números inteiro: '))
    if numero % 2 == 0:
        inicio += numero
        print(f'soma dos números  pares {inicio}')
    else:
        print(f'números impares não serão calculads!')
print('=-'* 9 + ' FIM DA OPERAÇÃO' + 8 * '-=')
# FEITO PELO PROFESSOR GUANABARA
soma = 0
cont = 0
for c in range(1,7):
    num = int(input(f'Digite o {c} valor?: '))
    if num% 2 == 0:
        soma += num
        cont += 1
print(f'Você somour {cont} e a soma foi {soma}')