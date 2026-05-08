'''frase = str(input('Digite qualquer frase: '))
maiúscula = frase.upper()
contar = maiúscula.count('A')
primeiro_a = maiúscula.find('A')
última_vez = maiúscula.rfind('A')
print('A frase tem {} letras (a) \nA primeira letra a fica posicionado em {} letra da frase da frase\nA Última letra *A* aparece em: {} letra da frase'.format(contar,primeiro_a,última_vez))
'''

frase = str(input('Digite uma frase: ')).strip()
print('A letra a aparece {} vezes na frase'.format(frase.upper().count('A')))
print('A primeira letra A apareceu na posição: {}'.format(frase.upper().find('A')+1))
print('A última aaA aparece na posição: {}'.format(frase.upper().rfind('A')+1))