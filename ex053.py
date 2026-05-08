frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = '' # ou inverso = junto[::-1] sem for
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo')
else:
    print('Não é um palindrome')
print(f'{junto}, {inverso}')