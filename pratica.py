def contador(ini, fim, pas):
    for c in range(ini, fim, pas):
        print(f"{c}",end=" ")
    print()


print('a) De 1 até 10, de 1 em 11')
contador(1,11, 1)

print("De 10 até 0, de 2 em 2 ")
contador(10,0, -2)