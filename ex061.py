#FEITO POR MIM pequeno erro o termo deve ser atibuído por outra var por ex.: primeiro_termo = termo e em soma primeiro_termo+=razao assim o programa começará a soma no primeiro número digitado
termo = int(input('Digite o termo de (P.A.) Progressão Aritmética?: '))
razao = int(input('Digite a razão (P.A.) Progressão Aritmética?: '))
c = 1
'''for c in range(10):
    formula = termo + c * razao
    print(f'progressão {formula} -',end=' ')
print(' fim')'''
# PROGRESSÃO COM BOUCLE WHILE
while c <= 10:
    #formula = termo + c * razao: a formula soma o termo e o (c) que é o limite da progressão multiplicar por razão
    termo+=razao #Obs: Outra maneira de calcular o fatorial que é simplemente somando o termo mais razão progressivamente anté o (wheli c < 11: c+=1 limite da progressao
    print(f'{termo} ',end=' » ')
    c += 1
print('Fim')
# FEITO PELO GUANABARA: tem uma pouca diferença nom comço da variavel termo: primeiro e razao: termo = primeiro o começo
print('Gerador P.A.')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão do P.A.: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} » ',end='')
    termo+=razao
    cont+=1
print("FIM")