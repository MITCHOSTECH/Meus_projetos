""" Faça um programa que leia algo pelo teclado
# e mostra na tel O SEU TIPO PRIMITIVO
# E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELE
# Captura a entrada do usuário
entrada = input("Digite algo: ")

# Mostra o tipo primitivo da entrada
print(f"O tipo primitivo de '{entrada}' é: {type(entrada)}")

# Verifica se a entrada é um número
print(f"É um número? {entrada.isnumeric()}")

# Verifica se a entrada é alfabética
print(f"É alfabético? {entrada.isalpha()}")

# Verifica se a entrada é alfanumérica
print(f"É alfanumérico? {entrada.isalnum()}")

# Verifica se a entrada está em maiúsculas
print(f"Está em maiúsculas? {entrada.isupper()}")

# Verifica se a entrada está em minúsculas
print(f"Está em minúsculas? {entrada.islower()}")

# Verifica se a entrada é um espaço em branco
print(f"É um espaço em branco? {entrada.isspace()}")

# Verifica se a entrada está capitalizada (primeira letra maiúscula)
print(f"Está capitalizada? {entrada.istitle()}") """
""" PARTE 2 CURSO EM VIDEO
a =  input('Digite Algo: ')
print('O tipo primitivo desse valore é: ', type(a))
print('Só tem espaço: ', a.isspace())
print('É um número: ', a.isnumeric())
print('É Alfabeto: ', a.isalpha())
print('É Alfanumérico: ', a.isalnum())
print('Está em Maiúscula: ',a.isupper())
print('Está em minúscula: ',a.islower())
print('Está capitalizada: ',a.istitle()) """
# PARTE 3 EXERCÍCIOS MEUS
# Solicitar uma entrada do usuário
obj = input("Digite algo: ")

# Verificar o tipo primitivo
print('O tipo primitivo desse valor é: {}'.format(type(obj)))

# Verificar se está em maiúscula
print('Está em maiúscula?: {}'.format(obj.isupper()))

# Verificar se está em minúscula
print('Está em minúscula?: {}'.format(obj.islower()))
# Verifica se está em Alfanumérico
print('É Alfanumérico?: {}'.format(obj.isalnum()))
