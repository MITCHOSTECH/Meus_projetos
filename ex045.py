 #Feita por min
'''from random import randint
from time import sleep
print('{:#^50}'.format('\033[4:35mInstrucões do jogo:\033[m\n'))
print('{:#^50}'.format('\033[1:31mATENÇÃO!\033[m'))
jogar = int(input('\033[1:35m_Pedra ganha tesoura(Pedra quebra tesoura)\nTesoura ganha papel(Tesoura corta papel)\nPapel ganha pedra(Papel embrulha pedra)\033[m\n\033[1:34m1. PEDRA\n2. TESOURA \n3. PAPEL\033[m\n\033[1:35mJOGA\033[m:'))
pedra = 1
tesoura = 2
papel = 3
sleep(0.4)
print('JO')
sleep(0.80)
print('KEN')
sleep(1.10)
print('PO!!!!')
print('-='*20)
aleatoria = randint(1,3)

if jogar == pedra and aleatoria == 2:
    print('\033[1:35mPARABÉNS VENCEU! O JOGADOR, ESCOLHEU PEDRA\n\033[mCOMPUTADOR ESCOLHEU \033[1:31mTESOURA\033[m')
elif jogar == pedra and aleatoria == 1:
    print('\033[1:34mEMPATE\033[m,TENTE NA PRÓXIMA')
    print('COMPUTADOR ESCOLHEU \033[1:34mTESOURA\033[m E JOGADOR ESCOLHEU \033[1:33mTESOURA \033[m')
elif jogar == tesoura and aleatoria == 3:
    print('\033[1:34mPARABÉNS VENCEU!\033[m')
    print('COMPUTADOR ESCOLHEU \033[1:31mPAPEL\033[m\n O JOGADOR ESCOLHEU \033[1:34mTESOURA\033[m')
elif jogar == tesoura and aleatoria == 2:
    print('\033[1:34mEMPATE\033[m TENTE NA PRÓXIMA')
    print('COMPUTADOR ESCOLHEU \033[1:34mTESOURA\033[m O JOGADOR TAMBE ESCOLHEU \033[1:34mTESOURA\033[m')
elif jogar == papel and aleatoria == 1:
    print('\033[1:36mPARABÉNS VENCEU!\033[m')
    print('O COMPUTADOR ESCOLHEU \033[1:31mPEDRA\o33[m\n O JOGADOR ESCOLHEU\033[1:34mPAPEL\033[m')
elif jogar == papel and aleatoria == 3:
    print('\033[1:34mEMPATE\033[m TENTE NA PRÓXIMA')
    print('O COMPUTADOR ESCOLHEU \033[1:34PAPEL\033[m O JOGADOR TAMBÉM ESCOLHEU \033[1:34mPAPEL\033[m')
elif jogar > 3:
    print('\033[1:31mERRO!\033[m \033[1:34mLEIA AS INSTRUÇÕES\033[m')
else:
    print('\033[1:31mPERDEU \033[m \033[1:36mBOA CHANCE NA PRÓXIMA!\033[m')
'''
# FEITO PELO PROFESSOR
from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Suas opcões
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?: '))
print('JO')
sleep(1)
print('Ken')
sleep(1)
print('PO!!!!!!')
print('=-' * 15)
print(f'O computador escolheu {itens[computador]}')
print(f'Computador jogou {itens[jogador]}')
print('=-' * 15)
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGA INVÁLIDA!')
elif computador == 1:# computador jogou papel
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:# computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('computador venceu')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
print('BOA SOTE NA PRÓXIMA JOGADA')