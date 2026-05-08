m = 'M'
f = 'F'
sexo = ''
while sexo != m and sexo != f:
    sexo = str(input('Digite seu sexo [M/F]?: ')).strip().upper()
    if sexo != m and sexo != f:
        print('Invalido por favor.')
if sexo == m:
    print(f'O aluno tem sexo: [{sexo}] Mascu lino')
elif sexo == f:
    print(f'O aluno tem sexo[M/F]: [{sexo}] Feminino')
# FEITO PELO PROF GUANABARA
sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invºalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')