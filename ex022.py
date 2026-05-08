#FEITO POR MIN
'''nome = str(input('Digite o seu nome: '))
maiúscula = nome.upper()
minúscula = nome.lower()
conta_letra_sem_espaço = len(nome.replace(' ',''))
dividir_frase_por_vigula = nome.split()
conta_primeira_frase = len(dividir_frase_por_vigula[0])
print('Nome em maiúscula {} \n Nome em minúscula{} \n Contar lestras na frase sem contar com a virgula {} letras \n Dividir cada frase com espaço em virgula {} letras \n Contar letras do primeiro nome {} letras'.format(maiúscula,minúscula,conta_letra_sem_espaço,dividir_frase_por_vigula,conta_primeira_frase))'''

# FEITO POR PROFESSOR
nome = str(input('Digite o seu nome: ')).strip()
print('Analisando o seu nome...')
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('O seu nome en total tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))