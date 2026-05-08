from random import randint
from time import sleep
n = int(input('Digite aleatóriamento um número inteiro: '))

escolha = randint(0,5)
print('Processar....')
sleep(3)
if escolha == n:
    print('Bem jogado o Sr. Venceu')
else:
    print('Perdeu! tenta na próxima BOA SORTE')