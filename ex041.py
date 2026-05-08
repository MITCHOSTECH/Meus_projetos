from datetime import date
ano_atual = date.today().year
nome = str(input('Nome de atleta: ')).upper().strip().split()
ano_nasc = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasc


if idade <= 9:
    print('{} {} tem {} anos nasceu em {}, esta na classificação: <<MIRIM>>'.format(nome[0],nome[-1],idade,ano_nasc))
elif 10 >= idade and idade <= 14:
    print('{} esta na classe: <<INFANTIL>>'.format(nome,idade,ano_nasc))
elif idade == 15 or idade <= 19:
    print('{} tem {} anos naceu em {}, esta na classe: <<JUNIOR>>'.format(nome,idade,ano_nasc))
elif idade == 20:
    print('{} tem {} anos nasceu em {}, esta na clase: <<SÊNIOR>>'.format(nome,idade,ano_nasc))
elif idade > 20:
    print('{} tem {} anos nasceu em {}, esta na calsse: <<MASTER>>'.format(nome,idade,ano_nasc))
elif idade > 59:
    print('{} tem {} anos nasceu em {}, não pode competir esta na idade da reforma'.format(nome,idade,ano_nasc))