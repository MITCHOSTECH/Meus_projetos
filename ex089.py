ficha = list()
while True:
    nome = str(input(f'Nome: '))
    nota1 = float(input(f'NOta1: '))
    nota2 = float(input(f'Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    rep = str(input(f'Quer continuar? [S/N]: ')).strip()[0]
    if rep in 'Nn':
        break
print('-=' * 30)
print(f"{'No.':<4}{'Nome':<10}{'Média':>8}")
print('-=' * 20)
for indice, aluno in enumerate(ficha):
    print(f"{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")
while True:
    print('-' * 30)
    opc = int(input(f'Mostrar notas de qual aluno?: (999 interrompe): '))
    if opc == 999:
        print(f'Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print(f'<<<VOLTE SEMPRE>>>')