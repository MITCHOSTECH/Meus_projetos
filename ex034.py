salario = float(input('Digite o seu salário: '))

if salario <= 1250:
    salario_minimo = salario + (salario * 15 / 100)
    print('O seu novo salário com 15% de aumento é de {},'.format(salario_minimo))
else:
    salario_maximo = salario + (salario * 10 / 100)
    print('O seu salário com 10% de aumento é de {}'.format(salario_maximo))