
from random import sample
n1 = str(input('Primeiro Aluo: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terciro Aluno: '))
n4 = str(input('Quarto Aluno: '))

nomes = [n1, n2, n3, n4]
escolhido = sample(nomes, k=4)
print('A ordem dos Alunos escolhido São: {}'.format(escolhido))

'''from random import shuffle

n1 = str (input('Primeiro aluno: '))
n2 = str (input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

nomes = [n1, n2, n3, n4]
sorteio = shuffle(nomes)

print('O sorteio aleatória de nomes dos alunos são:{}'.format(nomes))'''