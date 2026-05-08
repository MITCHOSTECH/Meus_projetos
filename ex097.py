opcao = " "
while opcao not in "N":
    def escreva(smg):
        print(f'{"="  * ( 2 + len(smg)):^40}')
        print(f'{smg:^40}')
        print(f'{'=' * ( 2 + len(smg)):^40}')


    #Programa principal
    escreva(str(input('Escreva uma frase: ')))
    opcao = str(input("Quer comtimuar? [S/N]: ")).strip().upper()[0]
    while opcao not in "NS":
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opcao in 'N':
        break


