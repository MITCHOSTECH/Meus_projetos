# Feito pelo guanabra
lista = list()
for c in range(0, 5):
    n = int(input('Digite umvalor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no fim da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('-=' * 30)
print(f"Os valores digitados em ordem foram: {lista}")

   #elif n > lista[len(lista)-1]: # ou lista[-1]
        #lista.append(n)
