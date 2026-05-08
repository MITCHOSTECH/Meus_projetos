'''# FEITO POR MIM
nome = str
idade = int
genero = str
media_idade = 0
idade_maior = 0
nome_homem = str
mulher_menos_de_vinte_anos = 0
for c in range(1,4+1):
    pessoa = 0
    pessoa +=c
    print(f"{'-' * 6}{pessoa}a Pessoa{'-' * 6}")
    nome = str(input('Nome Completo?: ')).capitalize().strip()
    idade = int(input('A sua idade?: '))
    genero = str(input('Genero (M/F)?: ')).upper().strip()
    media_idade += idade
    if idade > idade_maior and 'M' in genero:
        nome_homem = nome
        idade_maior = idade
    elif 'F' in genero and idade <= 19:
        mulher_menos_de_vinte_anos += 1
print(f'Idade total é {media_idade} anos com a média de idade do grupo é: {media_idade/4:.0f} anos')
print(f'Nome do homem mais velhom {nome_homem} tem {idade_maior} anos de idade')
print(f'{mulher_menos_de_vinte_anos} As Mulheres com menor de 20 anos de idade')
'''
#FEIOTO PELO PROF. GUANABARA
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
total_mulheres_menos_vinte = 0
for p in range(1,5):
    print(f'______{p}a Pessoa______')
    nome = str(input('Nome: ')).capitalize().strip()
    idade = int(input('Idade: '))
    genero = str(input('Sexo [M/F]: ')).upper().strip()
    soma_idade += idade
    if p == 1 and genero in 'Mm': # A operação in M eme maiúscula e m minúscula quer dizer que mesmo a pessoa degite: M ou m o programa compreederá
        maior_idade_homem = idade
        nome_homem_mais_velho = nome
    if genero  in 'Mm' and idade > maior_idade_homem:
        maior_idae_homem = idade
        nome_homem_mais_velhos = nome
    if genero in 'Mm' and idade < 20:
        total_mulheres_menos_vinte += 1
media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade}')
print(f'O homem mas velho chama-se {nome_homem_mais_velho} tem {maior_idade_homem} anos')
print(f'Em total são {total_mulheres_menos_vinte} com menor de 20 anos de idade')