from datetime import date
actual_data = date.today().year
nome = str(input('Nome completo:')).strip()
nasc = int(input('Ano de nascimento: '))
genero = str(input('Género (M/F): ')).upper()

idade = actual_data - nasc

print('{} nasceu em {} tem {} anos em {}.'.format(nome,nasc, idade, actual_data))
if idade == 18:
    print('Você te que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento '.format(saldo))
    ano_asseguir = actual_data + saldo
    print('Seu alistamento será em {}.'.format(ano_asseguir))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria se alistar há {} anos.'.format(saldo))
    ano_expirado = actual_data - saldo
    print('O Sr. deveria se alistar há {} anos'.format(ano_expirado))