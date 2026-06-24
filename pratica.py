from time import sleep
def contador(ini, fim, pas):
    if pas < 0:
        pas *= -1
    if pas == 0:
        pas = 1
    if ini < fim:
        cont = ini
        while cont <= fim:
            print(f'{cont}',end=" ")
            sleep(2)
            cont += pas
        print()
    else:
        cont = ini
        while cont >= fim:
            print(f'{cont}', end=" ")
            cont -= pas
#=================================
# Normal
#==================================
print('a) De 1 até 10, de 1 em 11')
contador(1,11, 1)
print()
print("b) De 10 até 0, de 2 em 2 ")
contador(10,0, -2)
print()
#==================================
# Personalizada
#===================================
inicio = int(input("Início: ")) + 1
fims = int(input("Fim: "))
passo = int(input("Passos: "))
contador(inicio, fims, passo)