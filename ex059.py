'''# FEITO POR MIM COM ERROS EM MULTIPLICAR E ENTRAR NOVOS VALORES
from time import sleep
soma = 0
multiplicar = int
maior = 0
novos_numeros = 4
sair_d_programa = 5
valores = float
menu = int
numeros_digitado = 1
for n in range(1,3):
    valores = float(input(f'Digite {numeros_digitado}o número  qualquer valor qualquer?: '))
    numeros_digitado+=1
    soma += valores
    multiplicar = valores * valores

print(''##########-MENU-############
[1]\033[34m Somar.\033[m
[2]\033[34m Multipicar\033[m
[3]\033[34m Maior\033[m
[4]\033[34m Novos números\033[m
[5]\033[34m Sair do programa\033[m
############################'')
while menu != sair_d_programa:
    menu = int(input('Que número de opção quer utlizar?: '))
    if menu == 1:
        print('A processar...')
        sleep(3)
        print(f'As somas  entre o primeiro número e o segundo é: {soma:.1f}')
    elif menu == 2:
        print('A processar...')
        sleep(3)
        print(f'A multiplicaçã entre O primeiro número e o segundo:= {multiplicar:.1f}')
    elif menu == 3:
        print('A processar...')
        sleep(3)
        if valores > maior:
            maior = valores
            print(f'Entre o primeiro e o segundo número o maior número é: {maior:.1f}')
    elif menu == 4:
        print('A processar...')
        sleep(3)
        for n in range(1, 3):
            valores = float(input(f'Digite {numeros_digitado}o número  qualquer valor qualquer?: '))
            numeros_digitado += 1
    else:
        print('A opção introduzida é inválido!')
print('Sair do programa...')
sleep(5)
print('FIM DO PROGRAMA!')'''
#FEITO PELO GUANABARA
from time import sleep
n1 = int(input('Primeiro valor?: '))
n2 = int(input('Segundo valor?: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('>>>>Qual é a sua opção?: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} = {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} = {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f'O maior número entre {n1} e {n2} é {maior}')
        elif n1 == n2:
            print(f'Não existe o número maior porque os dois número são iguais')
        else:
            maior = n2
            print(f'O maior número entre {n1} e {n2} é {maior}')
    elif opcao == 4:
        print('Informe os números novamente?')
        n1 = int(input('Primerio valor:'))
        n2 = int(input('Segundo valor:'))
    elif opcao == 5:
        print('Finalizando...')
        sleep(3)
    else:
        print('Opção inválida tente novamente!')
    print('=-=' * 10)
print('Fim do programa volte sempre')