a = int(input('Primeiro seguimento: '))
b = int(input('Segundo seguimento: '))
c = int(input('Terceiro seguimento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos podem formar um TRIÂNGULO', end=' ')
    if a == b == c: #Condições Aninhada
        print('EQUILÁTERO!')
    elif a != b!= c != a:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('OS SEGUIMENTOS NÃO PODEM FORMAR UM TRIÂNGULO')