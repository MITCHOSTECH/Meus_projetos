from datetime import datetime
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
print(voto(ano))