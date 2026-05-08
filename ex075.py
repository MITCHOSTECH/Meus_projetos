# FEITO POR MIM
'''cont_valor = 1
valores = (int(input('Digite 1 valor: ')),int(input('Digite 2 valor: ')),int(input('Digite 3 valores: ')),int(input('Digite 4 valor: ')))

print(f'O valores digitado são: {valores}')
print(f'O número 9 repeteu {valores.count(9)} vezes')
# ERO: Aqui tem que levar uma condição para verificar se o número 3 é executado se não o index por não incontrar o valor 3 vai dar ero e interroper a execução
print(f'O primeiro valor 3 foi digitado na {valores.index(3) + 1} posição')
for elementos in valores:
    if elementos % 2 == 0:
        print(f"Os números pares são: {elementos}, ",end='')
print('Fim de programa!')'''

# FEITO PELO GUANABARA
num = (int(input('Digite um número: ')),
       int(input('Digite  outro número número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite último número: ')))
print(f"Vocês digitou os valores: {num} ")
print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 in num:# essa condição é criada só se o número 3 foi executado(ATENÇÃO se o número 3 não foi executada ese bloco de condição não vai ser executado)
    print(f"o valor 3 apareceu na {num.index(3)+1} posição")
else:# (ATENÇÃO: sem essa condição, se não foi executado o valor 3 o index vai da ero e parar o programa automaticamente porque não incontrou o valor 3) então nesse caso em vez de dar ero o o bloco da  condição else: vai ser executado com uma mensagem que onúmero 3 não foi executado)
    print("O valor 3 não foi digitado em nenhuma posição")
print('Os valores pares digitados foram:  ', end=' ')
for elemento in num:
    if elemento % 2 == 0:
        print(elemento, end=' ')