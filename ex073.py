# FEITO POR MIM
'''campeonato_brasil = ('Atlético-MG','Bahia','Botafogo','Bragantino','Ceará','Corinthians','Cruzeiro','Flamengo','Fluminense','Fortaleza','Grêmio','Internacional','Juventude','Mirassol','Palmeiras','Santos','São Paulo','Sport','Vasco','Vitória')

for equipa in range(0,len(campeonato_brasil[:6])):
    print(f'Os cincos primeiros classificados são: {campeonato_brasil[equipa]}')

print(f'O último classificado é {campeonato_brasil[-1]}')
print(f'Os quatros últimos classificados são: {campeonato_brasil[-4:]}')
print(f'As listas de classificações em ordem alfabetica: {sorted(campeonato_brasil)}')'''
# FEITO PELO GUANABARA
times = ('Atlético-MG','Bahia','Botafogo','Bragantino','Ceará','Corinthians','Cruzeiro',
                     'Flamengo','Fluminense','Fortaleza','Grêmio','Internacional','Juventude','Mirassol',
                     'Palmeiras','Santos','São Paulo','Sport','Vasco','Vitória')
print('-=' * 15)
print(f'Lista de times {times}')
print('-=' * 15)
print(f'Os 5 primeiros times são: {times[:5]}')
print('-=' * 15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética : {sorted(times)}')
print('-=' * 15)
print(f" O Santos está na {times.index('Santos') + 1}")
