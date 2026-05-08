from time import sleep
nota1 = float(input('Entre a primeira nota: '))
nota2 = float(input('Entre a segunda nota: '))
print('A processar...')
sleep(3)
media = (nota1 + nota2) / 2

if media < 5:
    print('REPROVADO com a média de {:.2f}'.format(media))
elif media >= 5 and media <= 6.9: # 6.9 < media >= 5 : inferior a média superior a 5
    print('RECUPERAÇÃO com a média de {:.2f}'.format(media))
elif media >= 7:
    print('APROVADO com a média de {:.2f}'.format(media))
elif media == 0:
    print('A nota zérro é inválido')
print('aproveita nos estudos')



