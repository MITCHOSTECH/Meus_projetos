#FEITO PELO GUANABARA
''' print('=' * 30)
p\\ rint('{: ^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar: R$'))
total = valor
cedula_atual = 50
total_cedula = 0
while True:
    if total >= cedula_atual:
        total -= cedula_atual
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'O total de {total_cedula} cédulas de R${cedula_atual }')
        if cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1
        total_cedula = 0
        if total == 0:
            break
print('*' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
'''
# FEITO POR MIN
saque = int(input('Quanto quer sacar: '))
total_saque = saque
caixa = 50
saque_caixa = 0
while True:
    if total_saque >= caixa:
        total_saque -= caixa
        saque_caixa += 1
    else:
        if saque_caixa > 0:
            print(f'Foi sacado {saque_caixa} saque de {caixa} de cédula')
        if caixa == 50:
            caixa = 20
        elif caixa == 20:
            caixa = 10
        elif caixa == 10:
            caixa = 1
        saque_caixa = 0
        if total_saque <= 0:
            break
print('Fim')