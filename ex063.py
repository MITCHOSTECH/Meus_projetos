#FEITO POR MIM ERRADO
'''n_inteiro = int(input('Digite qualquer número inteiro para a sequência <<Fibonacci>>?: '))
n = 1
fibonacci = 0
while n < 10:
    fibonacci = (n_inteiro - n) + (n_inteiro -2)# A FÓRMULA DE FIBONACCI É: F(n) = f(n-1) + (n -2) que qer dizer em Python: [primeiramento os sinais nunca muda] O (n) é o inicio do boocle WHILE o n_inteiros = sera um variavel entroduzido pelo utilizado
    # O problema é que si executamos esta programa sem n_inteiro +=1 o resultados seria os números negativos que é erado  porque = o <n> que esta somar e adicionar com o n_inteiro esta em concatenação entao  em concatenação seria superior ao n_inteiro os resultados seria números negativos.
    n+=1
    n_inteiro += 1
    print(f'Os 10 primerios sequênci de Fibinacci do número \033[32m{n_inteiro}\033[m são: \033[34m{fibonacci}\033[m,')
print('Fim de programa!')'''
#FEITO PELO GUANABARA
print('-' * 30)
print('Sequência de finonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar?: '))
t1 = 0
t2 = 1
print(f'{t1} - {t2}',end='')
cont = 3 #O contador comecou no 3 porque já mostramos o primeiro e o segundo termo!
while cont <= n:
    t3 = t1 + t2
    print(f' - {t3}',end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' - FIM')