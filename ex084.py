# FEITO POR MIM
"""from time import sleep
list_prin = list()
seg_list = list()
cadastrada = 0
opcao = " "
while opcao not in "Nn":
    seg_list.append(str(input("Nome: ")))
    seg_list.append(float(input("Peso: ")))
    list_prin.append(seg_list[:])
    seg_list.clear()
    cadastrada += 1
    opcao = str(input("Quer continuar[S/N]: ")).strip()[0]
    while opcao not in "NnSs":
        opcao = str(input("Quer continuar[S/N]: ")).strip()[0]
maior = menor = 0
n_maior = n_menor = ""
l_maior = l_menor = 0
for pos, pessoa in enumerate(list_prin):
   if pos == 0:
       maior = menor = list_prin[pos][1]
   else:
       if list_prin[pos][1] > maior:
           maior = list_prin[pos][1]

       elif list_prin[pos][1] < menor:
            menor = list_prin[pos][1]


print(f" {'-=' * 10} Resolução dos exercícios {'-=' * 10}")
print(f"\nFOi cadastrada {cadastrada} {'Pessoas' if cadastrada <= 1 else 'Pessoas'}")
print(f"O maior peso é {maior}kg que pertence ao: ",end="")
for pos, pessao in enumerate(list_prin):
    if list_prin[pos][1] == maior:
        print(f"{list_prin[pos][0]}",end=",")

print(f"\nO menor peso é {menor}kg que pertence ao: ",end="")


for pos, pessoa in enumerate(list_prin):
    if list_prin[pos][1] == menor:
        print(f"{list_prin[pos][0]}",end=",")
print(f"\n")
for c in range(0,30):
    if c < 16:
        sleep(0.5)
        print(f"{'-='}",end='')
    else:
        if c == 16:
            sleep(1)
            print(f"\nFIM DO PROGRAMA",end='')
for c in range(0,3):
    sleep(1)
    print(f".",end='')"""

# FEITO PELO GUANABARA
temp = list()
princ = list()
maior = menor = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input("Quer continuar[S/N]: ")).strip()[0]
    if resp in 'Nn':
        break

print(f"No total cadastrou {len(princ)} pessoas")
print(f"O maior peso foi de {maior}kg. peso de ",end=' ')
for p in princ:
    if p[1] == maior:
        print(f"{p[0]}",end=',')
print()
print(f"O menor peso foi de {menor}kg. peso de ",end="")
for p in princ:
    if p[1] == menor:
        print(f"{p[0]}",end=",")
