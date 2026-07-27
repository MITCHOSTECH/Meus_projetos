#FEITO POR MIM
'''from datetime import datetime
ano_atual = datetime.now().year
def voto(idade):
    s_ano = ano_atual - idade
    if 18 <= s_ano <= 64:
        return f"Com {s_ano} anos: voto Obrigatório"
        #print(f'Com {s_ano} anos: voto é Obrigatório'.upper())
    elif s_ano < 18:
        return f"Com {s_ano} anos: voto Negado"
        #print(f'Com {s_ano} ano: voto negado'.upper())
    elif s_ano > 65:
        return f"Com {s_ano} anos: voto Opcional"
        print(f'com {s_ano} ano: voto opcional'.upper())




ano = int(input(f'Qual é o ano de nascimento: '))
#voto(ano)
print(voto(ano))'''

#FEITO PELO PROF GUANABARA
# from datetime import date -- não é necessário utilizar uma importação global se vai ser preciso numa só função-- ATENÇÃO


def voto(ano):
    from datetime import date # Escopo de variaveis --economize mais espaço ou mbs na memória
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA."
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"

nasc = int(input(f'Em que ano você nasceu? '))
print(voto(nasc))
