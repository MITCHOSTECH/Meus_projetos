'''#FEITO POR MIM
termo = float(input('Digite o primeiro termo?: '))
razao = int(input('Digite a razao?: '))
menu = 0
c = 1
termo_plus = 0
formula = termo

while termo != 0:
    formula = termo + c * razao
    while c <= 10 + termo_plus:
        formula = termo + c * razao
        c+=1
        print(f'Os dez primeiros termos são: de {c} é {formula:.0f}')
    print('#-'*8,'Menu' '#-'* 8)
    print('Prima tecla \033[34m[1]\033[m para mostrar mais termos?:\nPrima a tecla \033[34m[0]\033[mpara sair do programa?:')
    menu = int(input('\033[33mDigite aqui:____\033[m'))
    if menu == 1:
        termo_plus = int(input('Quantos termos deseja mostra?:'))
        print(f'Os {termo_plus} termos pedido por usuário são: {formula:.0f}')
    else:
        print('Fim do programa, O termo ºe igual a zero e TERMO não pode ser zero(0)!')
print('Fim do programa, O termo ºe igual a zero e TERMO não pode ser zero(0)!')
'''
# FEITO PELO GUANABARA
print('Gerador P.A.')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão do P.A.: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} » ',end='')
        termo+=razao
        cont+=1
    print("PAUSA")
    mais = int(input('Quanto termos você quer mostrar a mais?: '))
print(f'Progressão finalizada com {total} termos mostrado')